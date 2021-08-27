
variable "template_filepath" {
  default = "1"  # must not be blank
}

variable "template_string" {
  # should never be null, a string of length 0 means
  # we expect template_filepath to be set
  default = ""
}


# map of values, these will be json serialized
variable "template_variables" {}

variable "base64" {
  default = false
}

variable "output_filepath" {
  # optionally write result to a local file
  default = null
}
