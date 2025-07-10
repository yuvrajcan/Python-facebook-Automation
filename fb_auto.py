import facebook
access_token = 'EAACEdEose0cBAJd2nQO3wZDZD'
fb_obj = facebook.GraphAPI(access_token)
f_post = fb_obj.put_object(parent_object='me',connection_name='feed',message='Python code is working')
f_post
print('just posted on fb')
# Correct way to access the post ID
print(f_post['id'])

image_post=fb_obj.put_photo(image=open('download.jpeg','rb'),message='Python code just posted an image')
image_post
print(image_post)

post_comment = fb_obj.put_object(parent_object=image_post['post_id'],connection_name='comments',message='python is working')
post_comment

like_post = fb_obj.put_like(image_post['post_id'])
like_post

delete_post = fb_obj.delete_object(image_post['post_id'])
delete_post