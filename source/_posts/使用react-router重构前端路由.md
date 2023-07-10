---
title: 使用react-router重构前端路由
categories:
- 重构
---

# 重构前情况

因为公司的特点，开发人员没有太多区分，都是称为**通用软件开发工程师**。所以在工作中的看到的很多前端项目，都是有后端人员开发而来。所以在我们的代码中有很多后端程序思维写出的前端代码，而在一个项目中的路由情况尤为糟糕。

打开项目后看到的`router.js`代码：

```js
<HashRouter>
 <Route path="/" component={TempMgrView}/>
 ...
 <Route path="/settings" component={SettingView}/>
</HashRouter>
```

看起来是用了路由功能，实际上上面的路由配置都没有任何作用，真正的路由逻辑都在`TempMgrView`中:

```js
render(){
    let leftComponent = null;
    switch(this.state.path){
        case: "mgrView":
            left = <TempMgrView switchToSetting={switchToSetting}/>
            break;
        case: "setting":
            left = <SettingView switchToTempMgrView={switchToTempMgrView}/>
            break;    

    }
    return leftComponent;
}
```


