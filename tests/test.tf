
module "cloud_init" {
  source = "../"

  template_string = "NODE_NAME={{ node_name }}"
  template_variables = {
    node_name = "test"
  } 

  base64 = false
}

output "result" {
  value = module.cloud_init.rendered
}
