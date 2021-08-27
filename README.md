# terraform-jinja2-template

Terraform module for rendering jinja2 templates

### Usage:
```hcl
module "cloud-init-example-1" {

  source = "github.com/rossrochford/terraform-jinja2-template.git"

  template_filepath = "/home/ross/code/hashi_cluster/jinja_module_tf/cloud_init.tmpl"
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


output "result" {
  value = module.cloud-init-example-1.rendered
}
```