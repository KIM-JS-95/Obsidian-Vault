# .NET이란?

`.NET`은 Microsoft에서 개발한 소프트웨어 개발 플랫폼으로, 다양한 애플리케이션을 개발하고 실행할 수 있는 환경을 제공한다. 

`.NET`은 단순한 프레임워크가 아닌 프레임워크와 런타임 환경을 포함한 **종합적인 개발 플랫폼**으로  
초기에는 `.NET Framework`라는 이름으로 Windows 환경에 특화된 프레임워크로 시작했지만, 이후 크로스 플랫폼을 지원하는 `.NET Core`와 이를 통합한 `.NET 5` 이상 버전으로 발전하게 된다.

따라서 `.NET`은 특정 프레임워크를 넘어 다양한 애플리케이션 개발을 지원하는 **플랫폼**으로 이해하는 것이 적합합니다.

## 주요 특징
- **다양한 언어 지원**: C#, F#, VB.NET 등 여러 프로그래밍 언어를 지원
- **크로스 플랫폼**: .NET Core와 .NET 5 이상 버전은 Windows, macOS, Linux에서 실행 가능
- **풍부한 라이브러리**: 개발을 간소화하는 방대한 표준 라이브러리와 NuGet 패키지 관리 시스템을 제공
- **성능 최적화**: 고성능 애플리케이션 개발을 지원하며, JIT(Just-In-Time) 및 AOT(Ahead-Of-Time) 컴파일을 활용
- **오픈 소스**: .NET Core 이후로는 오픈 소스로 전환

## 구성 요소
- **.NET Runtime**: 애플리케이션 실행을 위한 런타임 환경.
- **ASP.NET**: 웹 애플리케이션 및 API 개발 프레임워크.
- **Entity Framework**: 데이터베이스와 상호작용하기 위한 ORM(Object-Relational Mapping) 도구.
- **Xamarin/MAUI**: 모바일 및 크로스 플랫폼 애플리케이션 개발 도구.

## 활용 사례
- **웹 애플리케이션**: ASP.NET Core를 사용한 고성능 웹사이트 및 API.
- **데스크톱 애플리케이션**: WPF(Windows Presentation Foundation) 및 WinForms.
- **클라우드 애플리케이션**: Azure와의 통합으로 클라우드 기반 솔루션 개발.
- **게임 개발**: Unity 엔진과 함께 사용.

.NET은 초보자부터 전문가까지 모두에게 적합한 강력한 개발 플랫폼으로, 생산성과 성능을 모두 제공하는 것이 특징입니다.

## .NET과 Spring 프레임워크의 차이점

| **특징**            | **.NET**                                         | **Spring Framework**                              |
|---------------------|-------------------------------------------------|-------------------------------------------------|
| **개발사**          | Microsoft                                       | Pivotal (현재 VMware)                           |
| **주요 언어**       | C#, F#, VB.NET 등                               | Java, Kotlin                                    |
| **크로스 플랫폼**   | .NET Core 및 .NET 5 이상에서 지원               | JVM이 지원되는 모든 플랫폼에서 실행 가능         |
| **오픈 소스 여부**  | .NET Core 이후 오픈 소스                        | 오픈 소스                                       |
| **주요 사용 사례**  | 웹, 데스크톱, 모바일, 클라우드, 게임 등 다양한 분야 | 주로 웹 애플리케이션 및 엔터프라이즈 솔루션 개발 |
| **의존성 관리**     | NuGet 패키지 관리 시스템                        | Maven, Gradle                                   |
| **생태계 및 지원**  | Microsoft 중심의 강력한 생태계와 지원            | 오픈 소스 커뮤니티 중심의 광범위한 생태계        |

## .NET의 IoC 컨테이너와 DI
`.NET`에서도 Spring Framework의 IoC 컨테이너와 유사한 개념이 존재하며, 이를 통해 **의존성 주입(Dependency Injection, DI)**을 지원합니다. 

### .NET에서의 DI 구현
`.NET`에서는 `Microsoft.Extensions.DependencyInjection` 네임스페이스를 통해 IoC 컨테이너와 DI를 구현할 수 있다. 
이 패키지는 ASP.NET Core를 포함한 다양한 `.NET` 애플리케이션에서 사용된다.

### 주요 기능
- **서비스 등록**: IoC 컨테이너에 서비스를 등록하여 의존성을 관리
- **생성자 주입**: 생성자를 통해 의존성을 주입
- **수명 주기 관리**: Singleton, Scoped, Transient 등 객체의 생명 주기를 관리

### sample code
```csharp
using Microsoft.Extensions.DependencyInjection;
using System;

public interface IGreetingService{
    void Greet(string name);
}

public class GreetingService : IGreetingService{
    public void Greet(string name){
        Console.WriteLine($"Hello, {name}!");
    }
}

class Program{
    static void Main(string[] args){
        // IoC 컨테이너 생성 및 서비스 등록
        var serviceCollection = new ServiceCollection();
        serviceCollection.AddTransient<IGreetingService, GreetingService>();
        var serviceProvider = serviceCollection.BuildServiceProvider();

        // 의존성 주입
        var greetingService = serviceProvider.GetService<IGreetingService>();
        greetingService?.Greet("World");
    }
}
```

### ASP.NET Core에서의 DI
ASP.NET Core에서는 DI가 기본적으로 내장되어 있으며, `Startup.cs` 파일의 `ConfigureServices` 메서드에서 서비스를 등록합니다.

```csharp
public void ConfigureServices(IServiceCollection services){
    services.AddControllers();
    services.AddTransient<IMyService, MyService>();
}
```

### .NET의 서비스 컨테이너와 Spring의 Bean 컨테이너 비교
| **특징**            | **.NET 서비스 컨테이너**                         | **Spring Bean 컨테이너**                          |
|---------------------|-------------------------------------------------|-------------------------------------------------|
| **주요 사용 방식**  | `ServiceCollection`을 통해 서비스 등록 및 주입   | `@Component`, `@Bean` 어노테이션을 통해 등록    |
| **수명 주기 관리**  | Singleton, Scoped, Transient                    | Singleton, Prototype, Request, Session 등       |
| **구성 방식**       | 코드 기반 구성                                   | 어노테이션 및 XML 기반 구성                     |
| **내장 여부**       | ASP.NET Core에 기본 내장                         | Spring Framework에 기본 내장                    |