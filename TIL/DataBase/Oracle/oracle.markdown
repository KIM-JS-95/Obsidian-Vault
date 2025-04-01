# ORACLE

`ORACLE`은 오라클 코퍼레이션에서 개발한 관계형 데이터베이스 관리 시스템(RDBMS)으로, 대규모 데이터 처리와 트랜잭션 관리에 강점을 가지고 있으며 안정성과 확장성이 뛰어나며, 기업 환경에서 널리 사용된다.

## PL/SQL(Procedural Language SQL)
`PL/SQL`은 ORACLE 데이터베이스에서 사용되는 절차적 언어로, 
SQL과 절차적 프로그래밍의 기능을 결합하여 복잡한 데이터베이스 작업을 수행할 수 있도록 한다. 

이를 통해 반복 작업, 조건문, 예외 처리 등을 구현할 수 있다.

`PL/SQL`은 이러한 절차적 언어의 특징을 가지며, SQL과 결합하여 데이터베이스 작업을 보다 유연하고 강력하게 수행할 수 있도록 설계되었다.

절차적 언어의 주요 특징:
- **순차적 실행**: 명령어가 작성된 순서대로 실행된다.
- **조건문과 반복문**: 조건에 따라 실행 흐름을 제어하거나 반복 작업을 수행할 수 있다.
- **모듈화**: <u>코드의 재사용성</u>을 높이기 위해 함수와 프로시저로 모듈화할 수 있다.
- **예외 처리**: 실행 중 발생하는 오류를 처리할 수 있는 메커니즘을 제공한다.

## ORACLE과 MySQL의 차이점

### 기능적 차이
- **ORACLE**: 대규모 데이터베이스와 복잡한 트랜잭션을 처리하는 데 적합하며, 고급 기능(예: 파티셔닝, 클러스터링, 고급 보안 옵션)을 제공한다.

- **MySQL**: 상대적으로 가벼운 데이터베이스로, 웹 애플리케이션과 같은 소규모 프로젝트에 적합하며, 오픈 소스 기반으로 비용 효율적이다.

### 문법적 차이

- **ORACLE**: `PL/SQL`을 사용하여 `절차적 프로그래밍`을 지원하며, 고급 기능과 데이터베이스 작업을 위한 다양한 내장 패키지를 제공한다.

- **MySQL**: `SQL`만을 사용하며, `절차적 프로그래밍`을 위해서는 외부 언어(예: Python, PHP)와의 연동이 필요하다.

### Sample Query

#### 반복작업 쿼리
```sql
DECLARE
    v_counter NUMBER := 1;
BEGIN
    WHILE v_counter <= 5 LOOP
        DBMS_OUTPUT.PUT_LINE('Counter: ' || v_counter);
        v_counter := v_counter + 1;
    END LOOP;
END;
/
```

#### 조건문
```sql
DECLARE
    v_salary NUMBER := 5000;
BEGIN
    IF v_salary > 4000 THEN
        DBMS_OUTPUT.PUT_LINE('High salary');
    ELSE
        DBMS_OUTPUT.PUT_LINE('Low salary');
    END IF;
END;
/
```

#### 예외처리
```sql
BEGIN
    -- Attempt to divide by zero
    DECLARE
        v_result NUMBER;
    BEGIN
        v_result := 10 / 0;
    EXCEPTION
        WHEN ZERO_DIVIDE THEN
            DBMS_OUTPUT.PUT_LINE('Error: Division by zero is not allowed.');
    END;
END;
/
```