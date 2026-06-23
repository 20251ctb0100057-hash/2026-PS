public class atividade28{

static double desc(double v,double p){
return v-(v*p/100);
}

static int maior(int x,int y){
return(x>=y)?x:y;
}

static double frete(double p){
if(p<=1){
return 10.0;
}else if(p<=5){
return 20.0;
}else{
return 35.0;
}
}

static int soma(int x,int y){
return x+y;
}

static double soma(double x,double y){
return x+y;
}

static void produto(String n){
System.out.println("Produto:"+n);
}

static void produto(String n,double pr){
System.out.println("Produto:"+n);
System.out.println("Preco:R$"+pr);
}

public static void main(String[]args){
System.out.println("\nProblema1");
System.out.println(desc(100,10));
System.out.println(desc(250,20));
System.out.println(desc(500,15));

System.out.println("\nProblema2");
System.out.println(maior(10,20));
System.out.println(maior(50,5));
System.out.println(maior(30,30));

System.out.println("\nProblema3");
System.out.println(frete(0.5));
System.out.println(frete(3));
System.out.println(frete(8));

System.out.println("\nProblema4");
System.out.println(soma(5,3));
System.out.println(soma(2.5,3.5));
System.out.println(soma(100,50));

System.out.println("\nProblema5");
produto("Refrigerante");
produto("Pizza",39.90);
produto("Hamburger",22.50);
}
}