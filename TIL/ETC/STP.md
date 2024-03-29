# 스패닝 트리 프로토콜
    스패닝 트리 알고리즘에 기반한 프로토콜로 `스위치` 에서 적용되는 프로토콜이다.

## STP를 이해하기 위한 2가지
1. 브리지 ID
    
    총 64비트(8바이트) 크기로 되어있어 Bridge Priority(16비트[2바이트], 유동), MAC Address(48바이트[6바이트], 고정)로 이루어져있다.


2. Path Cost
    장비 사이에 연결되어 있는 경로를 이용하기 위한 비용으로 브릿지의 거리 및 링크 속도를 알아내기 위한 값이다.

## STP의 구성

스패닝 트리는 단위 네트워크당 하나의 루트 브릿지를 가지며 

이를 제외한 나머지 `Non Root Bridge` 는 하나의 `루트 포트`를 가진다.

추가로 단위 세그먼트당 하나씩의 데지그네이티드<sup>*지정된</sup> 포트를 갖는다.

## STP 우선순위
1. 누가 더 작은 Root BID를 가지는가
2. 루트 브릿지로 향하는 Path cost는 누가 더 작은가
3. 누구의 BID가 작은가
4. 누구의 포트 ID가 작은가

## 대장 브릿지 선출

모든 스위치는 프로토콜에 따라 가장 먼저 Root 를 선출하도록 약속되어있다.

그렇기에 연결되어 있는 모든 스위치들이 가장먼저 하는 것은 `BPDU(Bridge Protocol Data Unit)` 교환으로 서로의 `BID`가 포함된 
정보를 교환하는 과정을 거치게 되며 낮은 BID , 즉 STP 우선순위 결정에 따라 루트 브릿지가 결정되며 이후 새로운 스위치가 연결된다면
`Root Bridge` 의 BID와 새로운 스위치의 BID를 교환하여 새로운 Root Bridge를 선출하게 된다.

### 우선순위를 변경하고 싶다면?
브릿지의 우선순위는 BID에 따라, 정확히는 BID가 가진 `Bridge Priority`에 따라 결정되지만 고정값이 아니기 때문에 
관리자에 의해 임의적으로 변경이 가능하다.

## 루트 포트 선출

`STP 우선순위` 2번째 규칙에 따라 