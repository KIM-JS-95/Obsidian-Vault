# CloudFront
Amazon CloudFront는 AWS(Amazon Web Services)에서 제공하는 `글로벌 콘텐츠 전송 네트워크(Content Delivery Network, CDN) 서비스`

CloudFront는 웹 사이트, 애플리케이션, 비디오 스트리밍 및 기타 콘텐츠를 사용자에게 더 빠르고 안전하게 전달하기 위해 설계되었습니다. 

## 주요 기능과 특징

1. **콘텐츠 전송 속도 향상**: CloudFront는 전 세계에 분산된 `Edge Location`을 사용하여 사용자와 가까운 위치에서 콘텐츠를 전달하여웹 페이지 로드 시간과 애플리케이션 응답 시간을 크게 줄일 수 있습니다.

2. **높은 가용성과 신뢰성**: CloudFront는 다중 엣지 로케이션을 통해 콘텐츠를 제공하며, 네트워크 장애가 발생하더라도 콘텐츠 전달이 중단되지 않도록 설계되어 있다.

3. **보안 기능**: CloudFront는 HTTPS를 통해 안전하게 콘텐츠를 전달하며, [[./AWS WAF]](Web Application Firewall)와 통합하여 애플리케이션을 보호할 수 있으며 DDoS(Distributed Denial of Service) 공격으로부터 보호하기 위한 [[./AWS Shield]]와도 통합된다.

4. **사용자 지정 가능한 콘텐츠 제공**: CloudFront는 사용자 지정 가능성이 뛰어나며, 콘텐츠 캐싱 정책, HTTP 헤더 조작, 사용자 지정 오류 페이지 등을 설정할 수 있다.

5. **스트리밍 기능**: CloudFront는 실시간 및 주문형 비디오 스트리밍을 지원한다. 이는 HLS(HTTP Live Streaming), DASH(Dynamic Adaptive Streaming over HTTP) 등 다양한 스트리밍 프로토콜을 지원하여 고품질의 스트리밍 경험을 제공한다.

6. **AWS 서비스와의 통합**: CloudFront는 Amazon S3, EC2, Elastic Load Balancing, Lambda 등 다양한 AWS 서비스와 통합되어 손쉽게 사용할 수 있으며 이를 통해 서버리스 환경에서도 콘텐츠를 효율적으로 제공할 수 있다.

7. **실시간 분석 및 모니터링**: CloudFront는 `실시간 로그 및 분석 기능을 제공`하여 콘텐츠 전달 성능을 모니터링하고 최적화할 수 있다.
 Amazon CloudWatch와 통합되어 성능 지표를 추적하고 경고를 설정할 수 있습니다.

