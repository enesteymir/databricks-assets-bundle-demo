def main():
    import argparse
    from datetime import timedelta, datetime
    from pyspark.sql import SparkSession
    from pyspark.dbutils import DBUtils


    # --- Get Wheel Parameters ---
    spark = SparkSession.builder.getOrCreate()
    dbutils = DBUtils(spark)
    parser = argparse.ArgumentParser()
    parser.add_argument('--day', type=str, help='Input data snapshot date YYYY-MM-DD')
    parser.add_argument('--env', type=str, help='Environment')
    args = parser.parse_args()

    default_date = (datetime.now() - timedelta(1)).strftime("%Y-%m-%d")

    env = args.env
    day = default_date if args.day in [None, "None"] else args.day

    print(f'This is a {env} job for the : {day}')
    
if __name__ == "__main__":
    main()
