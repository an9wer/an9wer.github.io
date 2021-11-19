在手机上使用 Pass 命令管理密码
==============================

:Published: : 2021/01/20

.. meta::
    :description: 在手机上使用 zx2c4 pass 命令。分别在安卓和苹果手机上安装、配置及使用，方便随时查看、修改及同步密码。

在 Linux 电脑上，我一直使用 `zx2c4's pass <https://www.passwordstore.org/>`_ 命令来管理密码。
最近和某位前同事聊天的时候，谈到了手机端密码管理的需求，想到自己平时偶尔也是需要在手机上输入密码；
不过每当这种时候，密码稍微复杂一点，我都是将手机通过 USB 线连接到电脑上之后，
使用 adb 命令 —— ``adb input text $(pass show <pass-name>)`` ，来处理的。
很明显，这样的方式太过麻烦，常常令我头大。


之前没发现 zx2c4's pass 居然还有移动端的客户端 ——
安卓上对应的是 `Password Store <https://github.com/android-password-store/Android-Password-Store>`_ APP，
于是开始在自己的安卓手机上下载、安装，并尝试配置使用。

Password Store 通过 clone git repository 的方式同步密码，
所以需要有个 git server，可以是类似 github 这种公共的仓库服务，也可以在本地创建一个私有仓库服务： ::

    $ cd <somewhere>
    $ mkdir password-store.git
    $ cd password-store.git
    $ git init --bare

然后同步本地 *~/.password-store* 目录下的所有内容到刚刚创建的 git server 中。
如果 *~/.password-store* 还不是一个 git repository，则需要先为其生成一个 git
repository： ::

    $ cd ~/.password-store
    $ git init
    $ git add .
    $ git commit -m "Initial commit"
    $ git remote add origin <username>@<hostname>:/path/to/password-store.git
    $ git push origin master

之后，在手机上打开 Password Store 软件，配置刚刚生成的 git server 的信息，
至于在同步 git repository 的时候通过何种方式认证，这里我选择了 ssh key： ::

    $ ssh-keygen -t ecdsa -f ~/.ssh/pass_ecdsa

    Transfer pass_ecdsa file to your phone, and open Password Store APP to import it.
    And then append content of ~/.ssh/pass_ecdsa.pub to ~/.ssh/authorized_keys file.

配置好上面这些之后就可以开始同步了，稍稍一会儿电脑上的 pass 密钥库就都同步到了手机上。
但是如何在手机 Password Store 上解密 pass 密钥文件呢？
此时则还需在手机上安装 `OpenKeychain <https://github.com/open-keychain/open-keychain>`_ APP，
然后将电脑上的 gnupg key 导入到 OpenKeychain 中： ::

    $ gpg --armor --export-secret-keys <key-name> | gpg --armor --symmetric --output <key-name>.sec.asc
    
    Transfer <key-name>.sec.asc to your phone, and open OpenKeychain APP to import it.

但是到了这一步之后，我发现还是无法解密 Password Store 中的密钥文件，
原因是需要在手机的设置中为 OpenKeychain 软件开启如下权限
（参考 `解决方案 <https://github.com/android-password-store/Android-Password-Store/issues/518#issuecomment-557832387>`_ )
： ::

    Settings -> Apps -> OpenKeychain -> Display pop-up windows while running in the background

至此，pass 命令终于可以在安卓手机上愉快地使用啦！

Updated 2021/11/18
------------------

最近开始用 iPhone 手机了，所以在 IOS 上也找了对应的 APP —— Pass，
其相对于安卓上的 Password Store 的优势是集成了 gnupg key 的管理，
因此无需另外一款类似 OpenKeychain 的 APP 配合使用。

Git repository 的同步和认证方式都与安卓的一样，只是 gnupg key 的导入同时需要
public key 和 secret key ::

    $ gpg --armor --export -o <key-name>.asc <key-name>
    $ gpg --armor --export-secret-keys -o <key-name>.sec.asc <key-name>

    Transfer <key-name>.asc and <key-name>.sec.asc to your phone, and open Pass APP to import it.

Thanks for reading :)
