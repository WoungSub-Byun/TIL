# AWS Essential(3)
- T academy AWS essential 강의
---

## AWS intro
---
### Amazon Web Services
**웹스케일**의 솔루션을 제공하고 IT 자원들을 탄력적, 효율적으로 비용관리 할 수 있는 **클라우드 제공자**

> **웹 스케일**
대규모의 환경에서도 높은 품질의 서비스를 비즈니스의 요구사항에 맞춰 신속하게 설계,구축 및 관리하는 패턴

#### 이점
- 민첩성, 즉각적인 탄력성
- 비용 절감 효과
- 개방성 및 유연성
- 보안
- 높은 기술 노하우

#### 대표 솔루션
- 어플리케이션 호스팅
- 웹 사이트
- 백업 및 스토리지
- 데이터베이스
- 엔터프라이즈 IT

### AWS Service Layer
![awscloudlayer](https://chetanspblog.files.wordpress.com/2017/09/aws-cloud-layer.jpg?w=525)

-  Bottom Level
AWS Global Pysical Infrastructure
물리적인 요소 - AWS 데이터 센터 설치된 지역들

- Low Level
    - Compute
        - EC2
        - Auto Scaling
    - Storage
        - S3
        - EBS(ElasticBeanstalk)
        - Glacler
    - Network
        - VPC
        - ELB
        - Route 53
    - Database
        - RDS(RDB)
        - DynamoDB(NoSQL)
        - ElastiCache
- High Level
    - Parallel Processing
        - Elastic MapReduce(Hadoop)
    - Transfer
        - Import Export VM
        - Import Storage Gateway
    - Content Delivery -> 한 컨텐츠에 대해 Edge까지 제공하기 위해 컨텐츠를 Cache해놓는 것
        - CloudFront
    - App Services
        - SNS
        - SWF
        - SES
    - Search
        - CloudSearch
        S3에 업로드한 데이터에 대해 서치인덱싱, 자동완성 등을 해주는 서비스
- Cross Service
    - Auth, Authorization, Federation
        - IAM
        계정에 특정 리소스에 접근 할 수 있는 권한을 부여하여 인증
        - MFA
    - Monitoring
        - CloudWatch
    - Deployment and Automation
        - Elastic Beanstalk
        - CloudFormation
        - Data Pipeline
- Tools to access services

### AWS 책임 분담 모델
![awsinfrastructure](https://image.slidesharecdn.com/07security-170324134647/95/aws-security-best-practices-march-2017-6-638.jpg?cb=1490363391)

- 물리적인 리소스들은 모두 AWS가 관리
- Firewall, OS, 보안, 플랫폼 등은 사용자가 관리해야함