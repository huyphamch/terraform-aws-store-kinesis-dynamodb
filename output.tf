# Output the Kinesis stream ARN
output "kinesis_stream_arn" {
  value = aws_kinesis_stream.realtime-data-stream.arn
}

# Output the Lambda function ARN
output "lambda_function_arn" {
  value = aws_lambda_function.realtime_data_consume.arn
}