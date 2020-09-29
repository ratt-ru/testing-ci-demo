from setuptools import setup, find_packages



setup(
    author="Simon Perkins",
    author_email='sperkins@ska.ac.za',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Testing CI Demo",
    extras_require={
    documentation
        'docs': ['numpydoc', 'sphinx']
        'testing': ['pytest', 'pytest-flake8', 'black'],
    },
    install_requires=['numpy'],
    license="BSD-3-Clause",
    #long_description="readme",
    #long_description_content_type='text/x-rst',
    #include_package_data=True,
    keywords='testing',
    name='testing-ci-demo',
    packages=find_packages(),
    python_requires=">=3.6",
    #setup_requires=setup_requirements,
    #test_suite='tests',
    #tests_require=test_requirements,
    #url='https://github.com/ska-sa/codex-africanus',
    version='0.0.1',
    zip_safe=False,
)
