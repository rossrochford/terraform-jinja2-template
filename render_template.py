import base64
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


def _base64_encode(st):
    st_bytes = st.encode("ascii")
    base64_bytes = base64.b64encode(st_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string


def main(stdin):
    di = json.loads(stdin)

    assert di['base64'] in ('true', 'false')
    encode_as_base64 = True if di['base64'] == 'true' else False

    ctx_data = json.loads(di['template_variables_json'])

    if len(di['template_string']) > 0:
        st = do_template_render__string(di['template_string'], ctx_data)
    else:
        st = do_template_render__file(di['template_filepath'], ctx_data)

    if encode_as_base64:
        st = _base64_encode(st)

    print(json.dumps({"rendered_result": st}))


if __name__ == '__main__':
    main(sys.stdin.read())
