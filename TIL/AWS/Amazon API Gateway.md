# Amazon API Gatewawy

Amazon API Gateway는 규모와 관계없이 REST 및 WebSocket API를 생성, 게시, 유지, 모니터링 및 보호하기 위한 AWS 서비스입니다.

API 개발자는 AWS 또는 다른 웹 서비스를 비롯해 AWS 클라우드에 저장된 데이터에 액세스하는 API를 생성할 수 있습니다.

API Gateway API 개발자는 자체 클라이언트 애플리케이션에서 사용할 API를 생성할 수 있습니다. 또는 타사 앱 개발자가 API를 사용하도록 제공할 수도 있습니다. 


## API gateway 개념

API Gateway는 다음을 지원하는 AWS 서비스입니다.

백엔드 HTTP 엔드포인트, AWS Lambda 함수 또는 기타 AWS 서비스를 노출하기 위한 RESTful 애플리케이션 프로그래밍 인터페이스(API)의 생성, 배포 및 관리.

AWS Lambda 함수 또는 기타 AWS 서비스를 노출하기 위한 WebSocket API의 생성, 배포 및 관리.

프런트 엔드 HTTP 및 WebSocket 엔드포인트를 통해 노출된 API 메서드 호출.

- API Gateway REST API
백엔드 HTTP 엔드포인트, Lambda 함수 또는 기타 AWS 서비스와 통합되어 있는 HTTP 리소스와 메서드의 모음입니다. 이 모음을 하나 이상의 스테이지로 배포할 수 있습니다. 일반적으로 API 리소스는 애플리케이션 로직에 따른 리소스 트리로 정리되어 있습니다. 각 API 리소스는 API Gateway에서 지원하는 전용 HTTP 동사가 있는 API 메서드를 하나 이상 표시할 수 있습니다. 자세한 내용은 REST API와 HTTP API 중에서 선택 단원을 참조하십시오.

- API Gateway HTTP API
백엔드 HTTP 엔드포인트 또는 Lambda 함수와 통합된 라우팅 및 메서드의 모음입니다. 이 모음을 하나 이상의 스테이지로 배포할 수 있습니다. 각 라우팅은 API Gateway에서 지원되는 고유의 HTTP 동사를 가진 API 메서드를 하나 이상 노출할 수 있습니다. 자세한 내용은 REST API와 HTTP API 중에서 선택 단원을 참조하십시오.

- API Gateway WebSocket API
백엔드 HTTP 엔드포인트, Lambda 함수 또는 기타 AWS 서비스와 통합되어 있는 WebSocket 경로와 경로 키의 모음입니다. 이 모음을 하나 이상의 스테이지로 배포할 수 있습니다. API 메서드는 프런트 엔드 WebSocket 연결을 통해 호출되며, 이 엔드포인트를 등록된 사용자 지정 도메인 이름과 연결할 수 있습니다.

- API 배포
API Gateway API의 특정 시점 스냅샷. 클라이언트가 사용할 수 있게 하려면 배포가 하나 이상의 API 단계와 연결되어 있어야 합니다.

- API 개발자
API Gateway 배포를 소유한 AWS 계정(예: 프로그래밍 액세스도 지원하는 서비스 공급업체)입니다.

- API 엔드포인트
특정 리전에 배포되는 API Gateway의 API 호스트 이름. 호스트 이름은 {api-id}.execute-api.{region}.amazonaws.com 형식을 갖고 있습니다. 다음 API 엔드포인트 유형이 지원됩니다.

엣지 최적화 API 엔드포인트/ 프라이빗 API 엔드포인트/ 리전 API 엔드포인트
