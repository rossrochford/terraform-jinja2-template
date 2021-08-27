import json
import os
import sys

import jinja2



def do_template_render__file(template_fp, json_data):
    base_path, filename = template_fp.rsplit('/', 1)
    template_loader = jinja2.FileSystemLoader(searchpath=base_path)
    template_env = jinja2.Environment(loader=template_loader, lstrip_blocks=True)
    template = template_env.get_template(filename)

    return template.render(**json_data)


def do_template_render__string(template_str, data):
    rtemplate = jinja2.Environment(loader=jinja2.BaseLoader).from_string(template_str)
    return rtemplate.render(**data)


def main(stdin, template_filepath):
    di = json.loads(stdin)

    ctx_data = json.loads(di['template_variables_json'])

    if len(di['template_string']) > 0:
        st = do_template_render__string(di['template_string'], ctx_data)
    else:
        st = do_template_render__file(template_filepath, ctx_data)

    print(json.dumps({"rendered_result": st}))


if __name__ == '__main__':
    main(sys.stdin.read(), sys.argv[1])