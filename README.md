# Python project template

Python is a versatile language that can be easy to use but challenging to master. 
Some common difficulties developers face when working with Python include project structuring and packaging, 
dependency management, and object-oriented programming.

To address these issues, I have sought solutions and resources to improve my Python development skills. 
One of the best resources I have found is (James Bennett's Boring Python series)[https://www.b-list.org/], which offers robust strategies for managing dependencies and improving code quality.
I have created a Python project template based on the Boring Python approach to implement these concepts. 

This template incorporates the best practices and recommendations outlined in Bennett's blog posts, helping me to create well-organized, reliable, and maintainable Python projects.
By applying the principles of Boring Python and other best practices, 
I aim to become a more skilled and efficient Python developer, 
tackling even the most complex programming challenges with confidence and ease.

## How to use this template

1. Fork the repository
2. Use as template for Python projects
3. Alter the dev and prod requirements.in file with the packages as needed
4. Run $MAKE$ to install for the appriopriate environment

Running 

```bash
$ make install
```
Will install the basic packages like pip-tools and pre-commit.

While running

```bash
$ make install-dev
```

Will install the packaged needed for the development environment.
