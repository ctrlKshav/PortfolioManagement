import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;
import java.util.InputMismatchException;
import java.util.Random;
// import java.util.*;

//A Class to represent a single share
class Stock{

    //General Attributes of a Stock
    String stockName,stockSector;
    double stockPrice,stockPERatio;
    long marketCap;
    int stockQnt;

    Stock(){}
    public Stock(String stockName, String stockSector, double stockPrice, double stockPERatio, long marketCap) {
        this.stockName = stockName;
        this.stockSector = stockSector;
        this.stockPrice = stockPrice;
        this.stockPERatio = stockPERatio;
        this.marketCap = marketCap;
        stockQnt=0;
    }

    void getStockDetails(){
        System.out.println("Name : "+stockName);
        System.out.println("Sector : "+stockSector);
        System.out.println("Price : "+stockPrice);
        System.out.println("PE Ratio : "+stockPERatio);
        System.out.println("Market Capitalisation : "+marketCap+"cr");
    }
}

//Encapsulating the properties of a stock exchange into one class where all shares all listed
class StockExchange{

    String stockExchangeName;
    HashMap<String,Stock> stockExchange;

    StockExchange(String name){
        stockExchangeName=name;
        stockExchange=new HashMap<>();
    }
    
    //Method to list a new stock on a stock exchange
    void submitIPO(Stock stock){
        stockExchange.put(stock.stockName, stock);
    }

    //Method to print all Stock listed on the exchange
    void listAllStocks(){
        System.out.println();
        for(Map.Entry<String,Stock> stock : stockExchange.entrySet()){
            System.out.println(stock.getKey()+" - "+stock.getValue().stockPrice);
        }
        System.out.println();
    }

    //Method to print details of a particular stock
    void listStockDetails(String userStockName){

        System.out.println();
        if(stockExchange.containsKey(userStockName)){
            System.out.println(stockExchangeName);
            stockExchange.get(userStockName).getStockDetails();
        }
        
        else
            System.out.println("Stock Not Listed on the exchange");
        System.out.println();
    }
    
    //A method to update prices of all the stocks listed on the exchange
    //The prices are decreased or increased by 50rs randomly
    void updatePrices(){
        Random r = new Random();
        for(Map.Entry<String,Stock> stock : stockExchange.entrySet()){
            Stock temp=stock.getValue();
            double priceUpdate=(int)(100*r.nextDouble())-50;
            temp.stockPrice+=priceUpdate;
            // stockExchange.put(stock.getKey(), temp);
        }
    }
}

//Many brokerage firms like Zerodha,Groww,AngelOne offer free Demat Accounts for Trading Stocks
class DematAccount{

    String accHolder;
    double accBalance,grossProfit;
    HashMap<String,Stock> stockHoldings;
    StockExchange BSE,NSE;

    DematAccount(String AccHolder,StockExchange bse,StockExchange nse){
        BSE=bse;
        NSE=nse;
        this.accHolder=AccHolder;
        accBalance=0;
        grossProfit=0;
        stockHoldings = new HashMap<>();
    }

    void checkBalance(){
        System.out.println("Wallet : "+accBalance+" INR");
    }

    void depositMoney(double money){
        System.out.println(money+" INR deposited to your account");
        accBalance+=money;
    }

    void withdrawMoney(double money){
        if(money>accBalance)
            System.out.println("Insufficient Balance");
        
        else{
            System.out.println(money+" INR withdrawn from your account");
            accBalance-=money;
        }
    }

    //A method to view all the shares owned by the account holder
    void viewPortfolio(){
        System.out.println();
        if(stockHoldings.isEmpty())
            System.out.println("No Shares in your wallet :(");
        else{
            for(Map.Entry<String,Stock> stock : stockHoldings.entrySet()){
                System.out.println(stock.getKey()+" - "+stock.getValue().stockPrice+" : "+stock.getValue().stockQnt+" Shares");
            }
        }
        System.out.println();
}


    void buyStock(String userStock,int userStockQnt){
        
        if(BSE.stockExchange.containsKey(userStock)){

            //We buy only from the stock exchange which has the lowest price offered
            double orderAmtBSE = BSE.stockExchange.get(userStock).stockPrice*userStockQnt;
            double orderAmtNSE = NSE.stockExchange.get(userStock).stockPrice*userStockQnt;
            if(orderAmtBSE<orderAmtNSE){
                //If we don't have enough money in our wallet then we cancel the order
                if(orderAmtBSE>accBalance){
                    System.out.println("Buy Order Cancelled because of Insufficient Balance\n");
                }
                else{
                    accBalance=accBalance-orderAmtBSE;
                    //If we already have shares of the company than we just change it's quantity
                     if(stockHoldings.containsKey(userStock)){
                    stockHoldings.get(userStock).stockQnt+=userStockQnt;
                    }

                    //If it's a new stock we put the stock object in our stockHoldings hashmap
                    else{
                        Stock stock = new Stock(
                            BSE.stockExchange.get(userStock).stockName,
                            BSE.stockExchange.get(userStock).stockSector,
                            BSE.stockExchange.get(userStock).stockPrice,
                            BSE.stockExchange.get(userStock).stockPERatio,
                            BSE.stockExchange.get(userStock).marketCap);
                        stock.stockQnt+=userStockQnt;
                        stockHoldings.put(userStock,stock);
                    }
                    System.out.println(userStockQnt+" "+userStock+" shares bought from the Bombay Stock Exchange\n");

                }
            }
            //Same logic just for National Stock Exchange
            else{
                 if(orderAmtNSE>accBalance){
                    System.out.println("Buy Order Cancelled because of Insufficient Balance");
                }
                else{
                    accBalance=accBalance-orderAmtNSE;
                    if(stockHoldings.containsKey(userStock)){
                    stockHoldings.get(userStock).stockQnt+=userStockQnt;
                }
                else{
                   Stock stock = new Stock(
                        NSE.stockExchange.get(userStock).stockName,
                        NSE.stockExchange.get(userStock).stockSector,
                        NSE.stockExchange.get(userStock).stockPrice,
                        NSE.stockExchange.get(userStock).stockPERatio,
                        NSE.stockExchange.get(userStock).marketCap
                );
                
                    stock.stockQnt+=userStockQnt;
                    stockHoldings.put(userStock,stock);
                    System.out.println(userStockQnt+" "+userStock+" shares bought from the National Stock Exchange\n");
                }
            }
            }
        }
        else{
            System.out.println("Stock Not Listed on the Stock Exchange\n");
        }

    }

    void sellStock(String userstock,int userStockQnt){  
        if(stockHoldings.containsKey(userstock)){
            Stock stock=stockHoldings.get(userstock);
            if(stock.stockQnt<userStockQnt){
                System.out.println("Sell Order Cancelled because Insufficient Stock Quantity");
                return;
            }
            //The price at which we bought the shares
            double orderAmtOg=stockHoldings.get(userstock).stockPrice*userStockQnt;
            //The current price of the share on the exchange
            double orderAmt=BSE.stockExchange.get(userstock).stockPrice*userStockQnt;
            grossProfit+=(orderAmt-orderAmtOg);
            accBalance+=orderAmt;
            System.out.println(userStockQnt+" "+userstock+" shares sold");
            
            //If we want to sell all shares then we remove the share from the hashmap
            if(stock.stockQnt==userStockQnt){
                stockHoldings.remove(userstock);
            }
            //Or else we just change it's quantity
            else if(stock.stockQnt>userStockQnt){
                stock.stockQnt-=userStockQnt;
                // stockHoldings.put(userstock, stock);
            }
        }
        else
            System.out.println("Stock not available in your portfolio");
        
    }

    //Method to print the profit or loss incurred on the account holder after trading
    void calculateProfit(){
        System.out.println();
        if(grossProfit>0)
            System.out.println("Your Net Profit : "+grossProfit+" INR");
        
        else if(grossProfit<0)
            System.out.println("Your Net Loss : "+Math.abs(grossProfit)+" INR");
        
        else
            System.out.println("Your Net Profit is 0 INR");
        
        System.out.println();
    }
}

//Main Class
public class StockMarketPortfolioMgmt {
    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);

        //Creating the Bombay Stock Exchange and National Stock Exchange
        StockExchange BSE=new StockExchange("BSE");
        StockExchange NSE=new StockExchange("NSE");

        //Listing all the stocks on the exchange since I can't gather the real time stock market data for now
        BSE.submitIPO(new Stock("HDFC","Banking",1600,17,891377));
        BSE.submitIPO(new Stock("Kotak Mahindra","Banking",1800,11,347012));
        BSE.submitIPO(new Stock("Asian Paints","Paint",2841,9,272546));
        BSE.submitIPO(new Stock("Berger Paints","Paint",580,7,21977));
        BSE.submitIPO(new Stock("TCS","IT Services",3385,12,1238899));
        BSE.submitIPO(new Stock("Infosys","IT Services",1496,10,626510));
        BSE.submitIPO(new Stock("Bharti Airtel","Telecommunication",750,14,425246));
        BSE.submitIPO(new Stock("Sun Pharma"," Pharmaceuticals ",1000,15,230168));
        BSE.submitIPO(new Stock("Maruti Suzuki","Automobile",8764,16,312000));
        BSE.submitIPO(new Stock("UltraTech Cement","Cement",7500,114,190000));
        BSE.submitIPO(new Stock("Adani Enterprises","Trading",1600,7,178330));

        NSE.submitIPO(new Stock("HDFC","Banking",1603,17,891377));
        NSE.submitIPO(new Stock("Kotak Mahindra","Banking",1790,11,347012));
        NSE.submitIPO(new Stock("Asian Paints","Paint",2837,9,272546));
        NSE.submitIPO(new Stock("Berger Paints","Paint",586,7,21977));
        NSE.submitIPO(new Stock("TCS","IT Services",3375,12,1238899));
        NSE.submitIPO(new Stock("Infosys","IT Services",1499,10,626510));
        NSE.submitIPO(new Stock("Bharti Airtel","Telecommunication",754,14,425246));
        NSE.submitIPO(new Stock("Sun Pharma"," Pharmaceuticals ",998,15,230168));
        NSE.submitIPO(new Stock("Maruti Suzuki","Automobile",8754,16,312000));
        NSE.submitIPO(new Stock("UltraTech Cement","Cement",7512,114,190000));
        NSE.submitIPO(new Stock("Adani Enterprises","Trading",1610,7,178330));

        //Creating the Demat Account of Myself
        DematAccount dmt=new DematAccount("Keshav", BSE, NSE);
        System.out.println("Hello "+dmt.accHolder+"!!\nWelcome to Your Demat Account"); 
        
        //Main Workspace
        boolean loop=true;
        while(loop) {
            System.out.println("What's on your mind?");
            System.out.println("1. Check your Account balance");
            System.out.println("2. Deposit money to your account");
            System.out.println("3. Withdraw money from your account");
            System.out.println("4. View Your Portfolio");
            System.out.println("5. Buy some Shares");
            System.out.println("6. Sell some Shares");
            System.out.println("7. Check My Profit");
            System.out.println("8. View Shares listed on the Stock Exchange");
            System.out.println("9. View a specific Stock");
            System.out.println("10. Update Prices of Stocks listed on the Exchange");
            System.out.println("");
            System.out.println("Press 0 to exit the program");
            int choice;
            try{
            choice=sc.nextInt();
            } catch(InputMismatchException e){
                choice=-1;
            }
            sc.nextLine();
            switch(choice){
                case 1:
                    dmt.checkBalance();
                    break;
                    case 2:
                        System.out.println("Enter the Amount you want to deposit");
                    while(true){
                    try{
                        double amt=sc.nextDouble();
                        sc.nextLine();
                        dmt.depositMoney(amt);
                        break;
                    }catch(InputMismatchException e){
                        System.out.println("Enter Valid Amount");
                        sc.nextLine();
                        }

                }
                        break;
            
                case 3:
                    System.out.println("Enter the Amount you want to Withdraw");
                    while(true){
                    try{
                    double amt2 = sc.nextDouble();
                    sc.nextLine();
                    dmt.withdrawMoney(amt2);
                    break;
                }catch(InputMismatchException e){
                        System.out.println("Enter Valid Amount");
                        sc.nextLine();
                    }
                }
                    break;
                case 4:
                    dmt.viewPortfolio();
                    break;
                case 5:
                    System.out.println("Enter the Name of the stock you want to buy");
                    String stock=sc.nextLine().trim();
                    System.out.println("Enter the Quantity of the stock");
                    while(true){
                    try{
                    int qnt=sc.nextInt();
                    sc.nextLine();
                    dmt.buyStock(stock,qnt);
                    break;
                    }catch(InputMismatchException e){
                        System.out.println("Enter Valid Quantitiy");
                        sc.nextLine();
                    }
                }
                    
                    break;
                case 6:
                    System.out.println("Enter the Name of the stock you want to sell");
                    stock=sc.nextLine().trim();
                    System.out.println("Enter the Quantity of the stock");
                    while(true){
                    try{
                    int qnt2=sc.nextInt();
                    sc.nextLine();
                    dmt.sellStock(stock,qnt2);
                    break;
                    }catch(InputMismatchException e){
                        System.out.println("Enter Valid Quantity");
                        sc.nextLine();
                    }
                    
                }
                    break;
                case 7:
                    dmt.calculateProfit();
                    break;
                case 8:
                    System.out.println("Bombay Stock Exchange");
                   BSE.listAllStocks();
                   System.out.println("National Stock Exchange");
                   NSE.listAllStocks();
                    break;
                case 9:
                    System.out.println("Enter Stock Name");
                    String userStock=sc.nextLine();
                    
                    NSE.listStockDetails(userStock);
                    
                    BSE.listStockDetails(userStock);
                    break;
                case 10:
                    BSE.updatePrices();
                    NSE.updatePrices();
                    System.out.println("Prices Updated");
                    break;
                case 0:
                    loop=false;
                    break;
                default:
                    System.out.println("Invalid Choice");
            }
        }
    }
}
