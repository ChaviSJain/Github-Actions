variable "aws_region" {
  default = "ap-south-1"
}

variable "lambda_function_name" {
  default = "flask_lambda"
}

variable "lambda_source_code_hash" {
  description = "Base64-encoded SHA256 hash of the Lambda zip file"
  type        = string
  default     = ""
}
