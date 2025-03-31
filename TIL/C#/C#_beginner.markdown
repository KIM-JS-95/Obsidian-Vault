```markdown
# C# 객체 지향 프로그래밍 예제

C#은 객체 지향 프로그래밍(OOP)을 지원합니다. 아래는 클래스, 상속, 다형성 등을 사용하는 간단한 예제입니다.

```csharp
using System;

namespace OOPExample
{
    // 기본 클래스
    public class Animal
    {
        public string Name { get; set; }

        public Animal(string name)
        {
            Name = name;
        }

        public virtual void Speak()
        {
            Console.WriteLine($"{Name}이(가) 소리를 냅니다.");
        }
    }

    // Animal 클래스를 상속받는 Dog 클래스
    public class Dog : Animal
    {
        public Dog(string name) : base(name) { }

        public override void Speak()
        {
            Console.WriteLine($"{Name}이(가) 멍멍 짖습니다.");
        }
    }

    // Animal 클래스를 상속받는 Cat 클래스
    public class Cat : Animal
    {
        public Cat(string name) : base(name) { }

        public override void Speak()
        {
            Console.WriteLine($"{Name}이(가) 야옹합니다.");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Animal dog = new Dog("바둑이");
            Animal cat = new Cat("나비");

            dog.Speak(); // 바둑이이(가) 멍멍 짖습니다.
            cat.Speak(); // 나비이(가) 야옹합니다.
        }
    }
}
```

위 코드는 C#에서 객체 지향 프로그래밍의 기본 개념을 보여줍니다. `Animal` 클래스는 기본 클래스이며, `Dog`와 `Cat` 클래스는 이를 상속받아 각각 고유의 동작을 구현합니다.

# C#에서 Oracle 데이터베이스 연결하기

C#을 사용하여 Oracle 데이터베이스에 연결하려면 `Oracle.ManagedDataAccess` NuGet 패키지를 사용합니다. 아래는 Oracle 데이터베이스에 연결하고 데이터를 조회하는 간단한 예제입니다.

```csharp
using System;
using Oracle.ManagedDataAccess.Client;

class OracleConnectionExample
{
    static void Main(string[] args)
    {
        // Oracle 데이터베이스 연결 문자열
        string connectionString = "User Id=your_username;Password=your_password;Data Source=your_datasource";

        using (OracleConnection connection = new OracleConnection(connectionString))
        {
            try
            {
                // 연결 열기
                connection.Open();
                Console.WriteLine("Oracle 데이터베이스에 성공적으로 연결되었습니다.");

                // SQL 쿼리 실행
                string query = "SELECT * FROM your_table";
                using (OracleCommand command = new OracleCommand(query, connection))
                {
                    using (OracleDataReader reader = command.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            Console.WriteLine($"Column1: {reader["Column1"]}, Column2: {reader["Column2"]}");
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"오류 발생: {ex.Message}");
            }
        }
    }
}
```

## 주요 단계
1. **NuGet 패키지 설치**: `Oracle.ManagedDataAccess` 패키지를 설치합니다.
2. **연결 문자열 구성**: Oracle 데이터베이스의 사용자 이름, 비밀번호, 데이터 소스를 포함한 연결 문자열을 설정합니다.
3. **쿼리 실행**: `OracleCommand`와 `OracleDataReader`를 사용하여 데이터를 조회합니다.

위 코드는 Oracle 데이터베이스와의 기본적인 연결 및 데이터 조회 방법을 보여줍니다. 실제 사용 시에는 연결 문자열과 쿼리를 적절히 수정해야 합니다.

# C#으로 간단한 프로그램 만들기

아래는 C#을 사용하여 간단한 계산기를 구현하는 예제입니다. 이 프로그램은 사용자로부터 두 숫자와 연산자를 입력받아 결과를 출력합니다.

```csharp
using System;

class Calculator
{
    static void Main(string[] args)
    {
        Console.WriteLine("간단한 계산기 프로그램");
        
        try
        {
            // 첫 번째 숫자 입력
            Console.Write("첫 번째 숫자를 입력하세요: ");
            double num1 = Convert.ToDouble(Console.ReadLine());

            // 두 번째 숫자 입력
            Console.Write("두 번째 숫자를 입력하세요: ");
            double num2 = Convert.ToDouble(Console.ReadLine());

            // 연산자 입력
            Console.Write("연산자를 입력하세요 (+, -, *, /): ");
            char operation = Console.ReadKey().KeyChar;
            Console.WriteLine();

            // 계산 및 결과 출력
            double result = operation switch
            {
                '+' => num1 + num2,
                '-' => num1 - num2,
                '*' => num1 * num2,
                '/' => num2 != 0 ? num1 / num2 : throw new DivideByZeroException("0으로 나눌 수 없습니다."),
                _ => throw new InvalidOperationException("유효하지 않은 연산자입니다.")
            };

            Console.WriteLine($"결과: {result}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"오류 발생: {ex.Message}");
        }
    }
}
```

## 주요 기능
1. **사용자 입력**: `Console.ReadLine`을 사용하여 사용자로부터 숫자와 연산자를 입력받습니다.
2. **조건 처리**: `switch` 표현식을 사용하여 입력된 연산자에 따라 계산을 수행합니다.
3. **예외 처리**: 잘못된 입력이나 0으로 나누는 경우를 처리하기 위해 `try-catch` 블록을 사용합니다.

위 코드는 간단한 계산기의 기본 동작을 보여줍니다. 필요에 따라 기능을 확장하거나 사용자 인터페이스를 개선할 수 있습니다.