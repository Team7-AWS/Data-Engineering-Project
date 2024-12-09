#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import boto3
import pandas as pd
import io
import json
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Replace with your bucket and file details
    input_bucket = 'team7project'
    input_key = 'student-scores.csv'
    output_bucket = 'projecttransformeddata'
    output_key = 'transformed-student-scores.csv'

    try:
        logger.info("Fetching the dataset from S3...")
        # Fetch the dataset from S3
        response = s3.get_object(Bucket=input_bucket, Key=input_key)
        raw_data = response['Body'].read().decode('utf-8')
        logger.info("Successfully fetched the dataset.")

        logger.info("Loading the dataset into a Pandas DataFrame...")
        # Load the data into a Pandas DataFrame
        df = pd.read_csv(io.StringIO(raw_data))
        logger.info(f"Dataset loaded. Columns: {list(df.columns)}")

        # Use pandas.factorize to encode string columns as integers
        logger.info("Encoding string columns using pandas.factorize...")
        for column in df.columns:
            if df[column].dtype == 'object':  # Check if column is of type object (strings)
                df[column], _ = pd.factorize(df[column])
                logger.info(f"Factorized column: {column}")

        # Example Transformation: Add a new column
        if not df.empty:
            logger.info("Performing transformations on the dataset...")
            df['Total_Score'] = df.iloc[:, 2:].sum(axis=1)  # Assuming scores are in columns 2 onwards
            df['Performance_Category'] = df['Total_Score'].apply(
                lambda x: 'High' if x > 600 else ('Medium' if x > 400 else 'Low')
            )
            logger.info("Transformations completed successfully.")
        else:
            raise ValueError("The input CSV file is empty or improperly formatted.")

        logger.info("Saving the transformed data back to S3...")
        # Save the transformed data back to S3
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)
        s3.put_object(Bucket=output_bucket, Key=output_key, Body=csv_buffer.getvalue())
        logger.info(f"Data successfully saved to {output_bucket}/{output_key}")

        return {
            'statusCode': 200,
            'body': json.dumps(f'Data successfully transformed and saved to {output_bucket}/{output_key}')
        }

    except Exception as e:
        logger.error(f"Error encountered: {str(e)}", exc_info=True)
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

