def lambda_handler(event, context):
    print(json.dumps(event, indent=4))
    #JSON形式の戻り値を設定する
    return{
        'statusCode' : 200,
        'headers' : {
            'content-type' : 'text/html'
        },
        'body' : '<html><body><h1>Hello World!<h1></body></html>'
    }
