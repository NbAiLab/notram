import requests, json, os, argparse

def main(args):
    #Debug_APIKEY = "YbH8IBFUqxrGP9fUNzFtgtvV6M1d1VI46WdPfu4bvjc"
    req_url='https://data.regjeringen.no/api/v1/publikasjoner'

    #'stm', 'prp' eller 'nou'.
    for doctype in ['stm','prp','nou']:
        response = requests.get(req_url,
            params={'publikasjonTypeKode': doctype, 'api_key': args.api_key},
            headers={'Accept': 'text/json'}
        )

        response_json = response.json()

        for p in response_json['publikasjon_liste']:
            lang = p['sprak_type']['kode']
            file_format = ""

            valid_formats = []
            for f in p['format_type_liste']:
                valid_formats.append(f['kode'])

            if "xhtml" in valid_formats:
                file_format = "xhtml"
            elif "pdf" in valid_formats:
                file_format = "pdf"

            if file_format:            
                url =  p['publikasjon_base_url']+'.'+file_format
                save_dir = os.path.join(args.output_folder,file_format,p['sprak_type']['kode'])
                output_file_name = save_dir+"/"+doctype+"_"+p['page_id']+"."+file_format
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)
                d = requests.get(url)
                open(output_file_name, 'wb').write(d.content)
                
                print(f'Downloading {url}')
                print(f'Saving {output_file_name}')



#import pdb; pdb.set_trace()
def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output_folder', required=True, help='Output folder. Will overwrite it exists')
    parser.add_argument('-a', '--api_key', required=True, help='Please add an API-key from regjeringen.no')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)