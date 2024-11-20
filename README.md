# wabbitinc-hugo
Hugo files for wabbitinc website

to test locally:
```
hugo server
```

to publish:
- commit and push
- Automatically deployed at netlify.com
- [![Netlify Status](https://api.netlify.com/api/v1/badges/d91a952b-dd42-46f1-a789-ebb6f15eeb6b/deploy-status)](https://app.netlify.com/sites/suspicious-kalam-c9e593/deploys)


# Linking to smugmug
smugmug can create links from pictures in html, here's a regex to transform them into hugo shortcodes:

```
search:
<a href="(.*)"><img src="(.*)" alt.*$
replace:
[![Image]($2)]($1)
```

# cloning
After clone,
```
git submodule init
git submodule update
```