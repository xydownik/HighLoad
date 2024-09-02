Path: 'http://127.0.0.1:8000' opens page with the list of Posts
Path: 'http://127.0.0.1:8000/posts' opens page with the list of Posts with template
Path: 'http://127.0.0.1:8000/blog/posts' opens page with the list of Posts without template
Path: 'http://127.0.0.1:8000/posts/:id' opens page with details of the Post #id with templates
Path: 'http://127.0.0.1:8000/blog/posts/:id' opens page with details of the Post #id with templates
Path: 'http://127.0.0.1:8000/posts/:id/edit/' opens page to edit the post only if you are logged in, if you are not it redirects you to login page
Path: 'http://127.0.0.1:8000/posts/:id/delete/' opens page to verify the deletion of the post only if you are logged in, if you are not it redirects you to login page
*if you are logged in, but trying to edit/delete others' posts, it will open the page with corresponding message
Path: 'http://127.0.0.1:8000/posts/new' opens page to create a new Post
Path: 'http://127.0.0.1:8000/register/' opens page of registration
Path: 'http://127.0.0.1:8000/login/' opens login page
Path: 'http://127.0.0.1:8000/logout/' logs you out
Path: 'http://127.0.0.1:8000/hello' opens welcoming message


Structure:
Posts List------------------------|-------------------|----------------|
|                                 |                   |                |
V                                 V                   V                V
Post details                      Add a post          Login            Logout
|     |      |                         |                 |
Edit  Delete Comment             *if logged out     *if no account
|     |      |                         |                 |
*if logged out                     Login page      Registration page
\     |      /
  \   |    /
  Login page
       |
 *if no account
       |
Registration page
