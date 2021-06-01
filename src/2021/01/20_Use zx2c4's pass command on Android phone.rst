Use zx2c4's pass command on Android phone
=========================================

我在电脑上一直使用 `zx2c4's pass <https://www.passwordstore.org/>`_ 命令来管理
密码。最近和某位前同事讨论的时候，提到了手机端密码管理的需求，我平时偶尔需要在
手机上输入密码，但一般都是通过 ``adb input text $(pass show <pass-name>)`` 来处
理的，稍微麻烦了一些。后来发现 zx2c4's pass 居然还有移动端的客户端，于是在我的
安卓机上下载了 `Password Store
<https://github.com/android-password-store/Android-Password-Store>`_ 这个软件，
并配置使用。

Password Store 是通过 git repo 的方式来同步密码的，所以需要先创建 git server，
在本地创建一个名为 *password-store.git* 的 git server： ::

    $ mkdir password-store.git
    $ cd password-store.git
    $ git init --bare

同步本地的 *~/.password-store* 文件夹到 git server，需要将该文件夹变成 git repo
然后同步到 git server： ::

    $ cd ~/.password-store
    $ git init
    $ git add .
    $ git commit -m "Initial commit"
    $ git remote add origin <username>@<hostname>:/path/to/password-store.git
    $ git push origin master

之后在手机上打开 Password Store 软件，配置 git server 的信息，然后同步，这样
pass 密钥库就同步到手机上了。

但是如何在手机 Password Store 上解密 pass 密钥文件呢？这个时候还需要安装
`OpenKeychain <https://github.com/open-keychain/open-keychain>`_ 软件，然后将
电脑上的 gnupg key 导入到 OpenKeychain 软件中： ::

    $ gpg --armor --export-secret-keys <key-name> | gpg --armor --symmetric --output <key-name>.sec.asc
    
    Transfer <key-name>.sec.asc to your phone, and then use OpenKeychain to import it.

我在操作到了这一步之后发现还是无法解密 Password Store 中的密钥文件，但搜索找到
了 `解决方案
<https://github.com/android-password-store/Android-Password-Store/issues/518#issuecomment-557832387>`_
，需要在手机的设置中为 OpenKeychain 软件开启如下权限： ::

    Settings -> Apps -> OpenKeychain -> Display pop-up windows while running in the background

至此，手机上可以顺利读取 zx2c4's pass 的密钥，接下来可以愉快地在手机上使用了。

Thanks for reading :)
