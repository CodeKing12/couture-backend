def upload_image(file, file_name, category):
    import base64
    from imagekitio import ImageKit
    from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions
    from environ import Env

    env = Env()
    env.read_env()

    imagekit = ImageKit(
        private_key = env("IMAGEKIT_PRIVATE_KEY"),
        public_key = env("IMAGEKIT_PUBLIC_KEY"),
        url_endpoint='https://ik.imagekit.io/kings12525'
    )

    options = UploadFileRequestOptions(
        folder='/the_pot_shop/media/products',
        tags=['product', 'weed', category],
        is_private_file=False,
        use_unique_file_name=True,
    )

    upload_response = imagekit.upload_file(
        file= base64.b64encode(file).decode(),
        file_name= file_name,
        options=options
    )

    return upload_response
