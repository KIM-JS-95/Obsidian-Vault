## 1. **데이터 타입 차이**
| 개념 | Oracle | MySQL |
|------|--------|--------|
| 문자열 | `VARCHAR2(n)`, `CHAR(n)` | `VARCHAR(n)`, `CHAR(n)` |
| 숫자 | `NUMBER(p,s)`, `INTEGER`, `FLOAT` | `INT`, `BIGINT`, `DECIMAL(p,s)`, `FLOAT` |
| 날짜/시간 | `DATE`, `TIMESTAMP` | `DATE`, `DATETIME`, `TIMESTAMP` |
| 자동 증가 | `SEQUENCE` 사용 (`AUTO_INCREMENT` 없음) | `AUTO_INCREMENT` 사용 |

- Oracle은 `VARCHAR2`를 사용하지만, MySQL은 `VARCHAR`를 사용함.
- MySQL은 `AUTO_INCREMENT` 지원하지만, Oracle은 `SEQUENCE`로 대체.

---

## 2. **자동 증가 (Auto Increment)**
- **Oracle**
  ```sql
  CREATE SEQUENCE my_seq START WITH 1 INCREMENT BY 1;
  INSERT INTO users (id, name) VALUES (my_seq.NEXTVAL, 'John');
  ```
- **MySQL**
  ```sql
  CREATE TABLE users (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(100)
  );
  ```

---

## 3. **문자열 결합**
- **Oracle** → `||` 연산자 사용  
  ```sql
  SELECT 'Hello' || ' ' || 'World' FROM dual;
  ```
- **MySQL** → `CONCAT()` 함수 사용  
  ```sql
  SELECT CONCAT('Hello', ' ', 'World');
  ```

---

## 4. **LIMIT vs ROWNUM vs FETCH**
| 기능 | Oracle | MySQL |
|------|--------|--------|
| 상위 N개 조회 | `FETCH FIRST n ROWS ONLY` 또는 `ROWNUM` 사용 | `LIMIT n` 사용 |
| 특정 범위 조회 | `OFFSET m ROWS FETCH NEXT n ROWS ONLY` | `LIMIT m, n` 사용 |

- **Oracle**
  ```sql
  SELECT * FROM employees ORDER BY salary DESC FETCH FIRST 10 ROWS ONLY;
  ```
- **MySQL**
  ```sql
  SELECT * FROM employees ORDER BY salary DESC LIMIT 10;
  ```

---

## 5. **DELETE vs TRUNCATE**
- **Oracle**  
  ```sql
  DELETE FROM employees WHERE id = 10;
  TRUNCATE TABLE employees;
  ```
  - `DELETE`: 트랜잭션 롤백 가능
  - `TRUNCATE`: 롤백 불가

- **MySQL**
  ```sql
  DELETE FROM employees WHERE id = 10;
  TRUNCATE TABLE employees;
  ```
  - MySQL `TRUNCATE`도 일부 스토리지 엔진(InnoDB)에서는 롤백 가능

---

## 6. **JOIN 문법**
- **Oracle (ANSI JOIN)**
  ```sql
  SELECT e.name, d.dept_name
  FROM employees e
  INNER JOIN departments d ON e.dept_id = d.dept_id;
  ```
- **MySQL (동일)**
  ```sql
  SELECT e.name, d.dept_name
  FROM employees e
  INNER JOIN departments d ON e.dept_id = d.dept_id;
  ```

**→ JOIN 문법은 거의 동일함**

---

## 7. **NULL 처리**
| 개념 | Oracle | MySQL |
|------|--------|--------|
| NULL 비교 | `IS NULL`, `IS NOT NULL` 사용 | 동일 |
| NULL 값 합산 | `NVL(컬럼, 대체값)` | `IFNULL(컬럼, 대체값)` |

* **NVL: Null Value Logic**

- **Oracle**
  ```sql
  SELECT NVL(salary, 0) FROM employees;
  ```
- **MySQL**
  ```sql
  SELECT IFNULL(salary, 0) FROM employees;
  ```

---

## 8. **서브쿼리에서 UPDATE**
- **Oracle**
  ```sql
  UPDATE employees 
  SET salary = (SELECT AVG(salary) FROM employees)
  WHERE department_id = 10;
  ```
- **MySQL (일부 버전에서는 서브쿼리 제한 존재)**
  ```sql
  UPDATE employees 
  SET salary = (SELECT AVG(salary) FROM (SELECT * FROM employees) AS sub)
  WHERE department_id = 10;
  ```

---

## 9. **그룹 함수 사용 (GROUP BY)**
- **Oracle (모든 선택한 컬럼이 GROUP BY에 포함되어야 함)**
  ```sql
  SELECT department_id, COUNT(*) FROM employees GROUP BY department_id;
  ```
- **MySQL (기본적으로 `ONLY_FULL_GROUP_BY` 비활성화 시 그룹 아닌 컬럼도 조회 가능)**
  ```sql
  SELECT department_id, name, COUNT(*) FROM employees GROUP BY department_id;
  ```

---

## 10. **트랜잭션 & COMMIT**
- **Oracle**: `COMMIT`, `ROLLBACK`, `SAVEPOINT` 지원  
- **MySQL**: `InnoDB` 엔진에서 `COMMIT`, `ROLLBACK` 지원  
  ```sql
  START TRANSACTION;
  UPDATE employees SET salary = salary * 1.1 WHERE department_id = 10;
  COMMIT;
  ```

---

### ✨ **요약**
1. **데이터 타입**  
   - Oracle: `VARCHAR2`, `NUMBER`, `DATE`  
   - MySQL: `VARCHAR`, `INT`, `DATETIME`
2. **자동 증가**  
   - Oracle: `SEQUENCE`  
   - MySQL: `AUTO_INCREMENT`
3. **문자열 결합**  
   - Oracle: `||`  
   - MySQL: `CONCAT()`
4. **페이징**  
   - Oracle: `FETCH FIRST n ROWS ONLY`  
   - MySQL: `LIMIT n`
5. **NULL 처리**  
   - Oracle: `NVL()`  
   - MySQL: `IFNULL()`
6. **트랜잭션**  
   - Oracle: 기본적으로 트랜잭션 사용  
   - MySQL: `InnoDB`에서만 트랜잭션 지원

이 외에도 성능 튜닝, 인덱스, 저장 프로시저 등에서도 차이가 있지만, 위 내용이 기본적인 차이점이에요. 🚀