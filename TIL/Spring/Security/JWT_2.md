---
layout: post 
title:  "SPRING JWT 구현"
date:   2021-07-02 14:05:21 +0800 
tags: SpringBoot JWT
color: rgb(154,133,255)
subtitle: SPRING 보안 인증 구현
---

[[0-Spring-Security MOC.md]] · #spring/security <!-- moc-nav -->

 
## 목표
@Controller 페이지를 개설 후 JWT 토큰이 발급된 사용자만이 접근할 수 있도록
기능을 구성하여 접근 권한 관리하도록 한다.

## 구현

### 1. 멤버등록(회원가입) 구현
웹페이지 접근 이전에 사용자가 가입된 상태인지 확인하도록 한다.

구현은 CRUD 구현괴 유사하지만 보한 특성을 강화하기 위해 **Password**는 PasswordEncoder.encode 메소드를 통해 함수화 한다.

```java
@RestController
@RequiredArgsConstructor
public class MemberController {

    final MemberRepository memberRepository;
    final PasswordEncoder encode;

    @PostMapping("/api/member")
    public String saveMember(@RequestBody MemberDto memberDto) {
        memberRepository.save(Member.createMember(memberDto.getEmail(), encode.encode(memberDto.getPassword())));
        return "success";
    }

}

@Data
class MemberDto {
    private String email;
    private String password;
}
```


* Request
```
POST : http://localhost:8080/api/member
```
```json
{
    "email" : "user",
    "password" : "user"
}
```

* Response
```json
{
    "timestamp": "2021-07-02T15:36:46.098+0000",
    "status": 401,
    "error": "Unauthorized",
    "message": "UnAuthorized",
    "path": "/hello"
}
```

---

### 2. JWT 토큰 발급
웹 관점에서 본다면 등록된 사용자가 로그인할 경우 토큰을 부여하여 토큰 유효시간 동안 추가 로그인 없이 서비스를 이용할 수 있도록
구성하야한다. 웹을 빠져나가도 토큰 유효시간 동안 사용자는 로그인 상태를 유지하고 있어 해당 페이지에 재접속해도 사용자 정보를 유지할 수 있게 된다.

```java
@RestController
@CrossOrigin
public class JwtAuthenticationController {

    @Autowired
    private JwtTokenUtil jwtTokenUtil;

    @Autowired
    private JwtUserDetailsService userDetailService;

    @PostMapping("/authenticate")
    public ResponseEntity<?> createAuthenticationToken(@RequestBody JwtRequest authenticationRequest) throws Exception {
        final Member member = userDetailService.authenticateByEmailAndPassword
                (authenticationRequest.getEmail(), authenticationRequest.getPassword());
        final String token = jwtTokenUtil.generateToken(member.getEmail());
        return ResponseEntity.ok(new JwtResponse(token));
    }

}

@Data
class JwtRequest {

    private String email;
    private String password;

}

@Data
@AllArgsConstructor
class JwtResponse {

    private String token;

}
```

```java

@Component
public class JwtTokenUtil {

    private static final String secret = "jwtpassword";

    // 토큰 유효시간
    public static final long JWT_TOKEN_VALIDITY = 5 * 60 * 60;

    public String getUsernameFromToken(String token) {
        return getClaimFromToken(token, Claims::getId);
    }

    public <T> T getClaimFromToken(String token, Function<Claims, T> claimsResolver) {
        final Claims claims = getAllClaimsFromToken(token);
        return claimsResolver.apply(claims);
    }

    private Claims getAllClaimsFromToken(String token) {
        return Jwts.parser().setSigningKey(secret).parseClaimsJws(token).getBody();
    }

    private Boolean isTokenExpired(String token) {
        final Date expiration = getExpirationDateFromToken(token);
        return expiration.before(new Date());
    }

    public Date getExpirationDateFromToken(String token) {
        return getClaimFromToken(token, Claims::getExpiration);
    }

    public String generateToken(String id) {
        return generateToken(id, new HashMap<>());
    }

    public String generateToken(String id, Map<String, Object> claims) {
        return doGenerateToken(id, claims);
    }

    // 암호 구현의 만료시간, 암호화 방식을 설정하고 반환
    private String doGenerateToken(String id, Map<String, Object> claims) {
        return Jwts.builder()
                .setClaims(claims)
                .setId(id)
                .setIssuedAt(new Date(System.currentTimeMillis()))
                .setExpiration(new Date(System.currentTimeMillis() + JWT_TOKEN_VALIDITY * 1000))
                .signWith(SignatureAlgorithm.HS512, secret)
                .compact();
    }

    public Boolean validateToken(String token, UserDetails userDetails) {
        final String username = getUsernameFromToken(token);
        return (username.equals(userDetails.getUsername())) && !isTokenExpired(token);
    }

}
```

```java
@Service
public class JwtUserDetailsService implements UserDetailsService {

    @Autowired
    private PasswordEncoder passwordEncoder;

    @Bean
    public BCryptPasswordEncoder passwordEncoder() {
        BCryptPasswordEncoder bCryptPasswordEncoder = new BCryptPasswordEncoder();
        return bCryptPasswordEncoder;
    }

    @Autowired
    private MemberRepository memberRepository;

    @Override
    public UserDetails loadUserByUsername(String email) throws UsernameNotFoundException {
        Member member = memberRepository.findByEmail(email)
                .orElseThrow(() -> new UsernameNotFoundException(email));
        Set<GrantedAuthority> grantedAuthorities = new HashSet<>();
        grantedAuthorities.add(new SimpleGrantedAuthority(Role.USER.getValue()));
        if (email.equals("whatever you want a email")) {
            grantedAuthorities.add(new SimpleGrantedAuthority(Role.ADMIN.getValue()));
        }

        return new User(member.getEmail(), member.getPassword(), grantedAuthorities);
    }

    public Member authenticateByEmailAndPassword(String email, String password) {
        Member member = memberRepository.findByEmail(email)
                .orElseThrow(() -> new UsernameNotFoundException(email));

        if(!passwordEncoder.matches(password, member.getPassword())) {
            throw new BadCredentialsException("Password not matched");
        }

        return member;
    }

}
```

1. @RequestBody 에서 데이터(email, password)를 가져온다.
2. 데이터(email, password)를 확인한여 등록된 사용자인지 확인한다.
3. 데이터를 DB에서 조회후 등록된 사용자라면 구현한 jwtTokenUtil.generateToken 메소드를 통해 토큰을 생성하여 반환한다.

---

### 3. Authorized Check
토큰은 헤더에 포함되어 서버에 전송되게 되는데  Authorized 에 해당하는 **Bearer "your Token"** 의 형태로 전송되게 된다.
서버에서는 토큰은 유효성을 분석하여 상태를 반환하고 유효한 토큰일 경우에는 jwtTokenUtil.validateToken 메소드를 통해 페이지 http에 대한 request / response를
반환한다.

![1](https://user-images.githubusercontent.com/65659478/124305512-295ad100-dba0-11eb-9d51-358b33ab640b.png)

> Bearer ??
> 
> Authentication API의 인증 방법중 하나이며  RFC 6750에 표준명세서에 따라 고안된 인증 방식이다.
>
> 사용법
>
> GET /resource HTTP/1.1 Host: server.example.com Authorization: Bearer mF_9.B5f-4.1JqM

```java
@Component
public class JwtRequestFilter extends OncePerRequestFilter {

    @Autowired
    private JwtUserDetailsService jwtUserDetailService;

    @Autowired
    private JwtTokenUtil jwtTokenUtil;

    private static final List<String> EXCLUDE_URL =
            Collections.unmodifiableList(
                    Arrays.asList(
                        "/api/member",
                        "/authenticate"
                    ));

    @Override
    protected void doFilterInternal(HttpServletRequest request,
                                    HttpServletResponse response,
                                    FilterChain filterChain) throws ServletException, IOException {

        final String requestTokenHeader = request.getHeader("Authorization");

        String username = null;
        String jwtToken = null;

        if (requestTokenHeader != null && requestTokenHeader.startsWith("Bearer ")) {
            jwtToken = requestTokenHeader.substring(7);
            try {
                username = jwtTokenUtil.getUsernameFromToken(jwtToken);
            } catch (IllegalArgumentException e) {
                System.out.println("Unable to get JWT Token");
            } catch (ExpiredJwtException e) {
                System.out.println("JWT Token has expired");
            }
        } else {
            logger.warn("JWT Token does not begin with Bearer String");
        }

        if(username != null && SecurityContextHolder.getContext().getAuthentication() == null) {
            UserDetails userDetails = this.jwtUserDetailService.loadUserByUsername(username);

            if(jwtTokenUtil.validateToken(jwtToken, userDetails)) {
                UsernamePasswordAuthenticationToken authenticationToken =
                        new UsernamePasswordAuthenticationToken(userDetails, null ,userDetails.getAuthorities());

                authenticationToken.setDetails(new WebAuthenticationDetailsSource().buildDetails(request));
                SecurityContextHolder.getContext().setAuthentication(authenticationToken);
            }
        }
        filterChain.doFilter(request,response);
    }

    @Override
    protected boolean shouldNotFilter(HttpServletRequest request) throws ServletException {
        return EXCLUDE_URL.stream().anyMatch(exclude -> exclude.equalsIgnoreCase(request.getServletPath()));
    }

}
```

* Request
```
POST : http://localhost:8080/authenticate
```
```json
{
    "email" : "user",
    "password" : "user"
}
```

* Response(성공 / 실패)
```json
{
  "token": "eyJhbGciOiJIUzUxMiJ9.eyJleHAiOjE2MjUyNjMyNDksImlhdCI6MTYyNTI0NTI0OSwianRpIjoic3VwMmlzQGdtYWlsLmNvbSJ9.aC_kRlQrSDALt2gtwl2AXRWJRPMkGERDmvWRsAYZlx0FFBb_UGurlHSYPf7Z7RS_BvAn_mq9rgd6GHBi7UXIpA"
}
```

```json
{
  "timestamp": "2021-07-02T17:05:10.510+0000",
  "status": 401,
  "error": "Unauthorized",
  "message": "UnAuthorized",
  "path": "/authenticate"
}
```

---

### 4. UnAuthorized 처리
1. WebSecurityConfig를 구현하여 개발자가 원하는 웹 보안 수준을 설정한다.

```java
@Configuration
@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {

    @Autowired
    private AuthenticationEntryPoint jwtAuthenticationEntryPoint;

    @Autowired
    private UserDetailsService jwtUserDetailsService;

    @Autowired
    private JwtRequestFilter jwtRequestFilter;

    @Autowired
    private DataSource dataSource;

    @Autowired
    private PasswordEncoder passwordEncoder;

    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {

        auth.jdbcAuthentication().dataSource(dataSource);
        auth
                .userDetailsService(jwtUserDetailsService)
                .passwordEncoder(passwordEncoder);
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
                .csrf().disable()
                .authorizeRequests().antMatchers("/authenticate", "/api/member").permitAll()
                .anyRequest().authenticated()
                .and()
                .exceptionHandling()
                .authenticationEntryPoint(jwtAuthenticationEntryPoint)
                .and()
                .sessionManagement()
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS);

        http.addFilterBefore(jwtRequestFilter, UsernamePasswordAuthenticationFilter.class);
    }
}
```


```java
@Component
public class JwtAuthenticationEntryPoint implements AuthenticationEntryPoint {

    @Override
    public void commence(HttpServletRequest request,
                         HttpServletResponse response,
                         AuthenticationException e) throws IOException, ServletException {

        response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "UnAuthorized");
    }

}
```
인증이 실패한 사용자일 경우 Web에서 "UnAuthorized"를 반환 한다.

```json
{
    "timestamp": "2021-07-02T17:05:10.510+0000",
    "status": 401,
    "error": "Unauthorized",
    "message": "UnAuthorized",
    "path": "/authenticate"
}
```
---

### 접속

인가된 사용자가 접속하여 TOKEN은 가지고 있는 상태라면 원하는 페이지에 접속을 허가해야한다. 
* Request
```
GET : http://localhost:8080/hello
```

* Return
```
Hello World
```



## Gradle Setting
```
dependencies {
    testImplementation 'org.junit.jupiter:junit-jupiter-api:5.7.0'
    testRuntimeOnly 'org.junit.jupiter:junit-jupiter-engine:5.7.0'
    implementation 'io.jsonwebtoken:jjwt:0.9.1'

    implementation 'org.springframework.boot:spring-boot-starter-web'
    compile('com.h2database:h2')

    compile("org.springframework.boot:spring-boot-starter-data-jpa")
    compileOnly 'org.projectlombok:lombok'
    annotationProcessor 'org.projectlombok:lombok'
    testCompile('org.springframework.boot:spring-boot-starter-test')

    implementation 'org.springframework.boot:spring-boot-starter-security'
}

```
### MyCode
[JWT Token Repo](https://github.com/KIM-JS-95/FreeNote)

### 🧾Reference
1. [JSON 웹 토큰](https://ko.wikipedia.org/wiki/JSON_%EC%9B%B9_%ED%86%A0%ED%81%B0)
2. [JWT 구조](https://velog.io/@ayoung0073/springboot-JWT)
3. [spring-boot JWT 예제](https://sup2is.github.io/2020/03/05/spring-security-login-with-jwt.html)
4. [Bearer Authentication](https://gist.github.com/egoing/cac3d6c8481062a7e7de327d3709505f)