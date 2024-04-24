# dbt with Dagster

[refer](https://docs.dagster.io/integrations/dbt/using-dbt-with-dagster/set-up-dbt-project)

```
cd jaffle_dagster/

DAGSTER_DBT_PARSE_PROJECT_ON_LOAD=1 dagster dev
```

## part one: Set up the dbt project

- Download a dbt project
- Configure your dbt project to run with DuckDB
- Build your dbt project

### Step 1: Download the sample dbt project
```
pip install dagster-dbt dagster-webserver dbt-duckdb

mkdir tutorial-dbt-dagster
cd tutorial-dbt-dagster

git clone https://github.com/dbt-labs/jaffle_shop.git
```

### Step 2: Configure your dbt project to run with DuckDB

```
cd jaffle_shop
touch profiles.yml # edit file
```

### Step 3: Build your dbt project

- Run all the models, seeds, and snapshots in the project and store a set of tables in your DuckDB database.
```
dbt build
```

## part two: Load dbt models as Dagster assets

- Create a Dagster project that wraps your dbt project
- Inspect your Dagster project in Dagster's UI
- Build your dbt models in Dagster
- Understand the Python code in your Dagster project

### Step 1: Create a Dagster project that wraps your dbt project

- `dagster-dbt project scaffold` command tạo ra dự án Dagster trong bất kỳ thư mục nào. Nếu đó là một thư mục khác với thư mục chứa dbt_project.yml, thì cần cung cấp một giá trị cho tùy chọn `--dbt-project-dir` để Dagster biết nơi tìm kiếm dự án dbt.

```
dagster-dbt project scaffold --project-name jaffle_dagster
```

### Step 2: Inspect your Dagster project in Dagster's UI

- DAGSTER_DBT_PARSE_PROJECT_ON_LOAD tạo file manifest.json 1 lần khi deploy
```
cd jaffle_dagster/

DAGSTER_DBT_PARSE_PROJECT_ON_LOAD=1 dagster dev
```

### Step 3: Build your dbt models in Dagster

- Materialize all asset

### Step 4: Understand the Python code in your Dagster project


## part three: Define assets upstream of your dbt models

- Install the Pandas and DuckDB Python libraries
- Define an upstream Dagster asset
- In the dbt project, replace a seed with a source
- Materialize the assets using the Dagster UI

### Step 1: Install the Pandas and DuckDB Python libraries

```
pip install pandas duckdb pyarrow
```

### Step 2: Define an upstream Dagster asset

### Step 3: In the dbt project, replace a seed with a source

```
cd ..
rm seeds/raw_customers.csv
```

### Step 4: Materialize the assets using the Dagster UI

## part four: Add a downstream asset

- Install the plotly library
- Define a downstream asset that computes a chart using plotly
- Materialize the order_count_chart asset

### Step 1: Install the plotly library

```
pip install plotly
```

### Step 2: Define the order_count_chart asset

### Step 3: Materialize the order_count_chart asset


