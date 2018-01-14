# Spark 

## Working with unstructured data

* Find dir with CSV files
* Read in dir of files with `wholeTextFiles()` and get file count
```
files = sc.wholeTextFiles()
files.count()
```

* Convert list of files to DataFrame
```
filenames = files.toDF(['name', 'data'])
dispplay(filenames)
```

* Show only the names using select()
```
display(filenames.select('name'))
```

## Read CSV Data

* Format CSV data
```
# read in file using csv format
df = spark.read.load(path,
                    format='com.databricks.spark.csv', 
                    header='true',
                    inferSchema='true')

# show 20 rows
display(df)
```
* Select all countries
```
display(
    df
        .select('Country')
        .distinct()
        .orderBy('Country')
)
```

## Exploratory Data Analysis with Spark
* Calculate order details 
```
display(
  df
    .select(df["InvoiceNo"],df["UnitPrice"]*df["Quantity"])
    .groupBy("InvoiceNo")
    .sum()
  )
```

## Spark SQL
* Create table without schema using csv (infer)
```
CREATE TABLE  IF NOT EXISTS population_v_price
USING CSV
OPTIONS (path "/databricks-datasets/samples/population-vs-price/data_geo.csv", header "true", inferSchema "true");

/* check results */
select * from population_v_price limit 100;
```

* Create table with scheme
```
CREATE TABLE IF NOT EXISTS online_retail(
InvoiceNo string,
StockCode string,
Description string,
Quantity int,
InvoiceDate string,
UnitPrice double,
CustomerID int,
Country string)
USING CSV
OPTIONS (path "/databricks-datasets/online_retail/data-001/data.csv", header "true");

/* check results */
select * from online_retail limit 100;
```

## Querying with Spark SQL
* Query first 100
```
select *
from cogsley_sales_csv
limit 100;
```
* Join Data 
```
select CompanyName, IPOYear, Symbol, round(sum(SaleAmount)) as Sales
from cogsley_sales_csv
left join cogsley_clients on CompanyName = Name
group by CompanyName, IPOYear, Symbol
order by 1
```

```
select i.StateCode, round(sum(s.SaleAmount)) as Sales
from cogsley_sales_csv s
join state_info i on s.State = i.State
group by i.StateCode
```

## Streaming Analytics (Real Time Data Analysis)
* Micro Batching - a method to achieve real time analysis by chunking operations into small batches.