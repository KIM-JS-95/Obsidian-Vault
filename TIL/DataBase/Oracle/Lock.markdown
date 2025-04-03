## **🔒 오라클 데이터베이스에서 Lock (잠금) 개념**  

오라클 DB에서는 **동시성 제어(Concurrency Control)** 및 **데이터 무결성(Integrity)**을 보장하기 위해 **Lock(잠금)**을 사용합니다.  
Lock은 여러 사용자가 동시에 데이터를 수정할 때, 충돌을 방지하고 **일관성**을 유지하는 데 중요한 역할을 한다.
---

## **1️⃣ Lock의 종류**
오라클의 Lock은 크게 **DML(데이터 조작), DDL(데이터 정의), 수동 잠금**으로 구분

### **🟢 1. DML Lock (데이터 조작 잠금)**
트랜잭션이 `SELECT FOR UPDATE`, `INSERT`, `UPDATE`, `DELETE` 등을 실행하면 자동으로 적용

| Lock 유형 | 설명 |
|-----------|------|
| **Row-level Lock (TX)** | 특정 행을 수정할 때 발생 (TX - Transaction Lock) |
| **Table Lock (TM)** | 테이블 단위로 적용되는 잠금 |
| **DDL Lock (Sch-M)** | DDL 실행 시 테이블 구조를 보호 |

#### **✅ Row-level Lock (TX)**
- **특정 행만 잠금** → 동시성 유지가 용이함  
- `UPDATE`, `DELETE`, `SELECT FOR UPDATE` 시 자동 발생  
- **Commit/Rollback 시 해제됨**

```sql
UPDATE employees SET salary = salary + 1000 WHERE emp_id = 101;
-- 해당 행(emp_id = 101)만 잠금 (다른 트랜잭션은 이 행을 수정할 수 없음)
```

#### **✅ Table-level Lock (TM)**
- **테이블 전체 잠금** → 특정 트랜잭션이 완료될 때까지 다른 세션이 테이블 수정 불가  
- `INSERT`, `UPDATE`, `DELETE` 수행 시 자동 발생  
- **특정 행이 아니라 테이블 전체가 영향을 받음**

```sql
LOCK TABLE employees IN EXCLUSIVE MODE;
-- employees 테이블을 독점적으로 잠금 (다른 트랜잭션은 읽기만 가능)
```

### **🟢 2. DDL Lock (데이터 정의 잠금)**
DDL 문 (`ALTER`, `DROP`, `TRUNCATE`, `RENAME`) 실행 시 자동 발생  
- **DDL 실행 중 다른 트랜잭션이 테이블을 수정할 수 없음**  
- DDL 문 실행 후 **자동 Commit**이 발생하여 트랜잭션이 종료됨  

```sql
ALTER TABLE employees ADD (age NUMBER);
-- 다른 트랜잭션이 employees 테이블을 수정하려 하면 대기하게 됨
```

---

### **🟢 3. 수동 Lock (Manual Lock)**
사용자가 명시적으로 잠금을 설정할 수 있음.

#### **✅ SELECT FOR UPDATE (특정 행 잠금)**
- 조회한 행을 **수정할 준비**를 하면서, **다른 트랜잭션이 수정하지 못하도록 잠금**  
- **해당 행을 변경하려면 Commit 또는 Rollback이 필요함**

```sql
SELECT * FROM employees WHERE emp_id = 101 FOR UPDATE;
-- emp_id = 101 행이 잠김 (다른 트랜잭션에서 UPDATE 불가)
```

> **🚨 Deadlock 주의**  
> 여러 트랜잭션이 같은 행을 `SELECT FOR UPDATE`로 잠그면 교착 상태(Deadlock)가 발생할 수 있음.  

---

## **2️⃣ Deadlock (교착 상태)**
💥 **Deadlock(교착 상태)**란, 두 개 이상의 트랜잭션이 서로 상대방의 Lock 해제를 기다리면서 영원히 대기하는 상태를 의미함.  

### **💀 Deadlock 발생 예시**
🔸 **T1 트랜잭션**  
```sql
UPDATE employees SET salary = salary + 1000 WHERE emp_id = 101;
-- T1이 emp_id = 101을 잠금
```
🔸 **T2 트랜잭션**  
```sql
UPDATE employees SET salary = salary + 500 WHERE emp_id = 102;
-- T2가 emp_id = 102를 잠금
```
🔸 **T1에서 T2가 잠근 행을 수정하려 할 때**
```sql
UPDATE employees SET salary = salary + 500 WHERE emp_id = 102;
-- T2가 잠근 emp_id = 102 때문에 대기 상태 발생
```
🔸 **T2에서도 T1이 잠근 행을 수정하려 하면?**
```sql
UPDATE employees SET salary = salary + 1000 WHERE emp_id = 101;
-- T1이 잠근 emp_id = 101 때문에 대기 상태 발생 → Deadlock!
```

### **🚀 Deadlock 해결 방법**
1. **트랜잭션 실행 순서 일관성 유지** → 항상 동일한 순서로 데이터를 업데이트  
2. **트랜잭션 실행 시간 최소화** → Lock을 오래 유지하지 않도록 설계  
3. **Deadlock 감지 후 해결**  
   ```sql
   ALTER SYSTEM SET DEADLOCK_DETECTION = TRUE;
   ```

---

## **3️⃣ Lock 확인 및 해제 방법**
### **🔍 현재 Lock 상태 확인**
```sql
SELECT 
    l.session_id, 
    l.locked_mode, 
    o.object_name, 
    s.sid, 
    s.serial#
FROM v$locked_object l
JOIN dba_objects o ON l.object_id = o.object_id
JOIN v$session s ON l.session_id = s.sid;
```

### **🔓 특정 세션의 Lock 해제 (강제 종료)**
```sql
ALTER SYSTEM KILL SESSION 'sid,serial#' IMMEDIATE;
```

예를 들어, `sid = 100`, `serial# = 12345`인 세션을 강제 종료하려면:
```sql
ALTER SYSTEM KILL SESSION '100,12345' IMMEDIATE;
```

---

## **🔹 요약**
| Lock 유형 | 설명 |
|-----------|------|
| **Row-level Lock (TX)** | 특정 행만 잠금 (`UPDATE`, `DELETE` 시 발생) |
| **Table Lock (TM)** | 테이블 전체 잠금 (`LOCK TABLE ... IN EXCLUSIVE MODE`) |
| **DDL Lock** | `ALTER`, `DROP`, `TRUNCATE` 실행 시 자동 발생 |
| **SELECT FOR UPDATE** | 특정 행을 잠그고 수정 가능 |
| **Deadlock** | 두 개 이상의 트랜잭션이 서로의 자원을 기다리며 무한 대기하는 상태 |
