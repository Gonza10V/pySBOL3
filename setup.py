from setuptools import setup

setup(name='sbol3_for_pudu',
      version='1.0.0a1',
      description='Python implementation of SBOL 3 standard compatible with PUDU',
      python_requires='>=3.7',
      url='https://github.com/Gonza10V/pySBOL3',
      author='Gonzalo Vidal',
      author_email='gvidal1011@gmail.com',
      license='MIT License',
      # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
            # How mature is this project? Common values are
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            'Development Status :: 3 - Alpha',

            # Indicate who your project is intended for
            'Intended Audience :: Developers',

            # Pick your license as you wish (should match "license" above)
            'License :: OSI Approved :: MIT License',

            # Specify the Python versions you support here. In particular, ensure
            # that you indicate whether you support Python 2, Python 3 or both.
            'Programming Language :: Python :: 3 :: Only',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
      ],
      # What does your project relate to?
      keywords='synthetic biology',
      packages=['sbol3'],
      package_data={'sbol3': ['rdf/sbol3-shapes.ttl']},
      install_requires=[
            # Require at least rdflib 6.1.1, and allow newer versions
            # of rdflib 6.x
            'rdflib>=6.1.1,==6.*',
            'python-dateutil==2.7.4',
            'pyshacl~=0.21',
      ],
      test_suite='test',
      tests_require=[
            'pycodestyle~=2.10'
      ])
