data "external" "template_script" {

  program = ["python3", "${path.module}/render_template.py", var.template_filepath]
  query = {
    template_variables_json = jsonencode(var.template_variables)
    template_string = var.template_string
  }
}


resource "local_file" script {

  count = var.output_filepath == null ? 0 : 1

  content  = data.external.template_script.result.rendered_result

  filename = var.output_filepath
  depends_on = [data.external.template_script]
}


output "rendered" {
    value = data.external.template_script.result.rendered_result
}
