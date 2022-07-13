# terraform-jinja2-template

Terraform module for rendering jinja2 templates

note: this modules assumes you have python3 and jinja2 installed system-wide.

### Usage:
```hcl
module "cloud-init-example-1" {

  source = "github.com/rossrochford/terraform-jinja2-template.git"

  template_filepath = "/home/me/cloud_init.tmpl"
  template_variables = {
    node_name = "traefik-1"
    node_type = "traefik"
  }
}


module "cloud-init-example-2" {

  source = "github.com/rossrochford/terraform-jinja2-template.git"

  # template can be passed as a filepath or a string
  template_string = <<EOT

write_files:
- path: /etc/environment
  content: |
    NODE_NAME="{{ node_name }}"
    NODE_TYPE="{{ node_type }}"
EOT

  template_variables = {
    node_name = "traefik-1"
    node_type = "traefik"
  }

  # optionally: write result to a local file
  output_filepath = "/tmp/cloud-init.txt"
}


output "result_1" {
  value = module.cloud-init-example-1.rendered
}
```
