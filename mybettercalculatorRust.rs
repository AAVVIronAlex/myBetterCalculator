fn main() 
{
    println!("Hello, welcome to my Calculator");
    print!("Input either of these sum, difference, squareeq, multiply, division, root, power, percentage, squareofthesum, squareofthedifference, differenceofsquares, sin, cos and there are more coming soon: ");
    // Flushing the buffer
    std::io::Write::flush(&mut std::io::stdout()).unwrap();

    let mut question1 = String::new();
    std::io::stdin().read_line(&mut question1).unwrap();

    let mut a = String::new();
    let mut b = String::new();
    let mut c = String::new();

    // Trimming the string from newlines and spaces/tabs
    let question1 = question1.trim();

    if question1 == "sum" 
    {
        print!("Input a, for the a + b formula: ");
        std::io::Write::flush(&mut std::io::stdout()).unwrap();
        std::io::stdin().read_line(&mut a).unwrap();
        let a: f64 = a.trim().parse().unwrap();

        print!("Input b, for the a + b formula: ");
        std::io::Write::flush(&mut std::io::stdout()).unwrap();
        std::io::stdin().read_line(&mut b).unwrap();
        let b: f64 = b.trim().parse().unwrap();

        sum(a, b);
    } 
    
    else if question1 == "difference" 
    {
        print!("Input a, for the a - b formula: ");
        std::io::Write::flush(&mut std::io::stdout()).unwrap();
        std::io::stdin().read_line(&mut a).unwrap();
        let a: f64 = a.trim().parse().unwrap();

        print!("Input b, for the a - b formula: ");
        std::io::Write::flush(&mut std::io::stdout()).unwrap();
        std::io::stdin().read_line(&mut b).unwrap();
        let b: f64 = b.trim().parse().unwrap();

        difference(a, b);
    }

    else if question1 == "multiply" 
    {
        print!("Input a, for the a * b formula: ");
        std::io::Write::flush(&mut std::io::stdout()).unwrap();
        std::io::stdin().read_line(&mut a).unwrap();
        let a: f64 = a.trim().parse().unwrap();

        print!("Input b, for the a * b formula: ");
        std::io::Write::flush(&mut std::io::stdout()).unwrap();
        std::io::stdin().read_line(&mut b).unwrap();
        let b: f64 = b.trim().parse().unwrap();

        multiplication(a, b);
    }

    else if question1 == "division" 
    {
        print!("Input a, for the a / b formula: ");
        std::io::Write::flush(&mut std::io::stdout()).unwrap();
        std::io::stdin().read_line(&mut a).unwrap();
        let a: f64 = a.trim().parse().unwrap();

        print!("Input b, for the a / b formula: ");
        std::io::Write::flush(&mut std::io::stdout()).unwrap();
        std::io::stdin().read_line(&mut b).unwrap();
        let b: f64 = b.trim().parse().unwrap();

        division(a, b);
    }

    else
    {
        println!("Try again.");
    }
}

fn sum(a: f64, b: f64) 
{
    println!("a + b = {}", a + b);
}

fn difference(a: f64, b: f64)
{
    println!("a - b = {}", a - b);
}

fn multiplication(a: f64, b: f64)
{
    println!("a * b = {}", a * b);
}

fn division(a: f64, b: f64)
{
    println!("a / b = {}", a / b);
}