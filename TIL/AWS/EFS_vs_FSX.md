# Amazon EFS_vs_Amazon FSx

Amazon EFS (Elastic File System)와 Amazon FSx는 모두 AWS에서 제공하는 파일 시스템 서비스이지만, 그 목적과 사용 사례가 다름

## Amazon EFS (Elastic File System)

1. **사용 사례**:
   - 공유 파일 스토리지로,` 다수의 EC2 인스턴스가 동일한 파일 시스템을 동시에 액세스`할 수 있도록 설계
   - `Linux 기반 워크로드`에 최적화되어 있으며, 웹 서버, 콘텐츠 관리 시스템, 데이터 분석 등 다양한 용도로 사용

2. **성능 및 확장성**:
   - 자동으로 확장 및 축소되어 스토리지 용량을 관리할 필요가 없음
   - 두 가지 성능 모드: `표준 성능` 및 `최대 I/O 성능 모드`
   - 동적 스케일링을 통해 높은 스루풋을 제공하며, 많은 수의 EC2 인스턴스와 동시에 연결할 수 있습니다.

4. **비용**:
   - 사용한 스토리지 용량에 따라 비용이 발생합니다.
   - 비용은 GB-월 단위로 청구됩니다.

5. **지역 가용성**:
   - 여러 AWS 리전에서 사용 가능하며,`리전 간 데이터 액세스를 지원하지 않음`

## Amazon FSx

1. **사용 사례**:
   - 특정 워크로드에 최적화된 관리형 파일 시스템을 제공합니다.
   - Windows 기반 애플리케이션, 고성능 컴퓨팅(HPC), 머신 러닝, 백업 및 복구 등 다양한 용도로 사용됨

2. **파일 시스템 유형**:
   - **Amazon FSx for Windows File Server**: `Windows Server`를 기반으로 하며, SMB 프로토콜을 사용합니다. Windows 애플리케이션과의 호환성 및 Active Directory 통합을 지원

   - **Amazon FSx for Lustre**: 고성능 컴퓨팅 워크로드를 위한 병렬 파일 시스템으로, 대규모 데이터 집합에 대한 고속 I/O를 제공합니다. HPC, 빅 데이터 분석, 머신 러닝에 적합합니다.

3. **성능 및 확장성**:
   - **FSx for Windows File Server**: 단일 AZ 또는 여러 AZ에서 사용 가능하며, 성능을 용량 및 IOPS 수준에 맞게 조정할 수 있습니다.

   - **FSx for Lustre**: 높은 스루풋과 낮은 지연 시간을 제공하며, S3와의 통합을 통해 데이터 집합을 쉽게 관리할 수 있습니다.

4. **비용**:
   - 선택한 파일 시스템 유형 및 성능 수준에 따라 비용이 다릅니다.
   - GB-월 단위로 청구되며, 성능 수준에 따라 추가 비용이 발생할 수 있습니다.

5. **지역 가용성**:
   - 여러 AWS 리전에서 사용 가능하며, 파일 시스템 유형에 따라 다릅니다.

## 요약
- **Amazon EFS**는 `다수의 EC2 인스턴스가 동시에 접근 가능한 공유 파일 시스템을 제공`하며, Linux 워크로드에 최적화되어 있습니다.
- **Amazon FSx**는 특정 워크로드에 최적화된 파일 시스템을 제공하며, Windows 애플리케이션 및 고성능 컴퓨팅 워크로드를 지원합니다.

각 서비스의 특성을 이해하고, 필요에 따라 적합한 파일 시스템을 선택하는 것이 중요

```
Q. 
A solution architect needs to design a resilient solution Window users; home directories.
The solution must provide fault tolerance, file-level backup and recovery, and access control, based on the company's Active Directory.
Which storage solution meets these requirements?

A. Configure `Amazon EBS` to store the users home DIRs Configure [AWS Single Sign-on](./Single_Sign-on) with Active DIR

B. Configure `Amazon EFS` for the users home DIRs Configure [AWS Single Sign-on](./Single_Sign-on) with Active DIR

C. Configure Amazon S3 to store the users' DIRs. Join Amazon S3 to Active Directory

D. Configure a Multi-AZ file system with Amazon FSx for Window File Server Join Amazon FSx to to Active DIR

A.
Answer is `D`
 
```

