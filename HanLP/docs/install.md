# Install

```{figure} _static/install-versions.svg
---
width: 100%
figclass: caption
alt: HanLP versions
name: hanlp-versions
---
Choose your HanLP version
```

## Install RESTful Packages

[![Downloads](https://pepy.tech/badge/hanlp-restful)](https://pepy.tech/project/hanlp-restful) [![Downloads](https://pepy.tech/badge/hanlp-restful/month)](https://pepy.tech/project/hanlp-restful) [![Downloads](https://pepy.tech/badge/hanlp-restful/week)](https://pepy.tech/project/hanlp-restful) 

```{eval-rst}
.. margin:: **Beginners Attention**

    .. Hint:: New to NLP? Just install RESTful packages and call :meth:`~hanlp_restful.HanLPClient.parse` without pain.
```

For beginners, the recommended RESTful packages are easier to start with. 
The only requirement is [an auth key](https://bbs.hankcs.com/t/apply-for-free-hanlp-restful-apis/3178). 
We officially released the following language bindings:

### Python

```shell script
pip install hanlp_restful
```

### Java

See [Java instructions](https://hanlp.hankcs.com/docs/api/restful_java.html).

### Golang

See [Golang instructions](https://hanlp.hankcs.com/docs/api/restful_golang.html).

## Install Native Package

[![Downloads](https://pepy.tech/badge/hanlp)](https://pepy.tech/project/hanlp) [![Downloads](https://pepy.tech/badge/hanlp/month)](https://pepy.tech/project/hanlp) [![Downloads](https://pepy.tech/badge/hanlp/week)](https://pepy.tech/project/hanlp)  

The native package running locally can be installed via pip.

````{margin} **Install from Source**
```{note}
See [developer guideline](https://hanlp.hankcs.com/docs/contributing.html#development).
```
````

```
pip install hanlp
```

HanLP requires Python 3.6 or later. GPU/TPU is suggested but not mandatory. Depending on your preference, HanLP offers the following flavors:

````{margin} **Windows Support**
```{note}
Installation on Windows is **perfectly** supported. No need to install Microsoft Visual C++ Build Tools anymore. 
```
````

````{margin} **Apple Silicon**
```{note}
HanLP also perfectly supports accelerating on Apple Silicon M1 chips, see [tutorial](https://www.hankcs.com/nlp/hanlp-official-m1-support.html).
```
````

| Flavor  | Description                                                  |
| ------- | ------------------------------------------------------------ |
| default | This installs the default version which delivers the most commonly used functionalities. However, some heavy dependencies like TensorFlow are not installed. |
| tf      | This installs TensorFlow and fastText.                       |
| amr     | To support Abstract Meaning Representation (AMR) models, this installs AMR related dependencies like `penman`. |
| full    | For experts who seek to maximize the efficiency via TensorFlow and C++ extensions, `pip install hanlp[full]` installs all the above dependencies. |


## Install Models

In short, you don't need to manually install any model. Instead, they are automatically downloaded to a directory called [`HANLP_HOME`](https://hanlp.hankcs.com/docs/configure.html#customize-hanlp-home) when you call `hanlp.load`.
Occasionally, some errors might occur the first time you load a model, in which case you can refer to the following tips.

### Download Error

#### HanLP Models

If the auto-download of a HanLP model fails, you can either:

1. Retry as our file server might be busy serving users from all over the world.
1. Follow the message on your terminal, which often guides you to manually download a `zip` file to a particular path. 
1. Use a [mirror site](https://hanlp.hankcs.com/docs/configure.html#use-mirror-sites) which could be faster and stabler in your region.

#### Hugging Face 🤗 Transformers Models

If the auto-download of a Hugging Face 🤗 Transformers model fails, e.g., the following exception is threw out:

```bash
lib/python3.8/site-packages/transformers/file_utils.py", line 2102, in get_from_cache
    raise ValueError(
ValueError: Connection error, and we cannot find the requested files in the cached 
path. Please try again or make sure your Internet connection is on.
```

You can either:

1. Retry as the Internet is quite unstable in some regions (e.g., China).

2. Force Hugging Face 🤗 Transformers to use cached models instead of checking updates from the Internet **if you have ever successfully loaded it before**, by setting the following environment variable:

   ```bash
   export TRANSFORMERS_OFFLINE=1
   ```

### Server without Internet

If your server has no Internet access at all, just debug your codes on your local PC and copy the following directories to your server via a USB disk or something.

1. `~/.hanlp`: the home directory for HanLP models.
1. `~/.cache/huggingface`: the home directory for Hugging Face 🤗 Transformers.


### Import Error

Some TensorFlow/fastText models will ask you to install the missing TensorFlow/fastText modules, in which case you'll need to install the full version:

```shell script
pip install hanlp[full]
```

```{danger}
NEVER install thirdparty packages (TensorFlow/fastText etc.) by yourself, as higher or lower versions of thirparty packages have not been tested and might not work properly.
```