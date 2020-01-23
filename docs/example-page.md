# Example Page

## Prerequisites

- a `CentOS 6`, `CentOS 7` or `CentOS 8` `x86_64` linux distribution installed (it should also work with correponding RHEL or ScientificLinux distribution)
- (or) a `Fedora 29` or `Fedora 30` `x86_64` linux distribution
- (or) a `mageia 6` or `mageia 7` `x86_64` linux distribution
- (or) an `opensuse/leap:15.0`, `opensuse/leap:15.1`, `opensuse/leap:42.3` `x86_64` linux distribution (it should also work with corresponding SLES distribution)

!!! success "Portable RPMs"
    As we build "reasonably portable" RPM packages, it should work with any RPM based linux distribution
    more recent than `CentOS 6` linux distribution (2011).

!!! tip "We :heart: CentOS"
    As we develop MetWork Framework mainly on `CentOS` linux distributions, this is
    our recommendation if you can choose your OS.

!!! info
    We are working right now on supporting other Linux distributions (debian, ubuntu). Please contact us if you
    are interested in.

- disabled `SELinux`

??? question "How to do that?"
    To disable `SELinux` on a `CentOS` Linux distribution, which is enabled by default, you have to change the file
    `/etc/selinux/config` to set `SELINUX=disabled`, then reboot the system.

??? question "I don't want to disable SELinux!"
    It should work with enabled `SELinux` but we never tested so **tests, comments and help are welcome**.

- internet access to metwork-framework.org (on standard TCP/80 port)

??? question "Offline install?"
    Of course, you can deploy on a computer without internet access but you will have to build your own
    mirror or you will have to install correspondings RPM files manually (not difficult but a little boring).

## Configure the metwork RPM repository

### Check

First check the output of `uname -a |grep x86_64`. If you have nothing, you don't have a `x86_64` distribution installed and you can't install MetWork on it.

### Choose a version

Depending on your needs (stability versus new features), you can choose between several versions :

- released stable versions with a standard [semantic versionning](https://semver.org/) `X.Y.Z` version number *(the more **stable** choice)*, we call it **released stable**
- continuous integration versions of the release branch *(to get future **patch** versions before their release)*, we call it **continuous stable**
- continuous integration of the `master` branch *(to get future **major** and **minor** versions before their release)*, we call it **continuous master**
- continuous integration of the `integration` branch *(the more **bleeding edge** choice)*, we call it **continuous integration**

For each version, you will find the `BaseURL` in the following table:

Version | BaseURL
------- | -------
released stable | http://metwork-framework.org/pub/metwork/releases/rpms/stable/portable/
continuous stable | http://metwork-framework.org/pub/metwork/continuous_integration/rpms/stable/portable/
continuous master | http://metwork-framework.org/pub/metwork/continuous_integration/rpms/master/portable/
continuous integration | http://metwork-framework.org/pub/metwork/continuous_integration/rpms/integration/portable/

??? question "Want to install a released old version ?"
    You have to change the `BaseURL` and replace `/stable/` by `/release_X.Y/`. For example, use
    `http://metwork-framework.org/pub/metwork/releases/rpms/release_0.9/portable/`
    as `BaseURL` for installing a `0.9.Z` released old version.

??? question "Want to install a < 0.9 version?"
    Before `0.9` version, the `portable` subdirectory did not exist, it was replaced
    by `centos6` and `centos7` directory with dedicated builds inside. If you are
    using a `< 0.9` version, please change `portable` by the corresponding value.

### Configure

**For CentOS and Fedora distributions**, to configure the metwork RPM repository,
you just have to create a new `/etc/yum.repos.d/metwork.repo` with the following
content (example for a **released stable** version):

```cfg
[metwork_stable]
name=MetWork Repository Stable
baseurl=http://metwork-framework.org/pub/metwork/releases/rpms/stable/portable/
gpgcheck=0
enabled=1
metadata_expire=0
```

If you prefer to copy/paste something, you can do that with following root commands
(still for a **released stable**):

```bash
cat >/etc/yum.repos.d/metwork.repo <<EOF
[metwork]
name=MetWork Repository
baseurl=http://metwork-framework.org/pub/metwork/releases/rpms/stable/portable/
gpgcheck=0
enabled=1
metadata_expire=0
EOF
```

??? question "For Mageia distributions?"
    To configure the metwork RPM repository for Mageia distributions, use the following `root` command:
    ```console
    urpmi.addmedia metwork http://metwork-framework.org/pub/metwork/releases/rpms/stable/portable/
    ```

??? question "For SUSE distributions?"
    To configure the metwork RPM repository for SUSE distributions, use the following `root` command:
    ```console
    zypper ar -G http://metwork-framework.org/pub/metwork/releases/rpms/stable/portable/ metwork
    ```

!!! warning
    Previous examples are about stable release. **Be sure
    to change the `baseurl` value if you want a "non stable" MetWork version.**


### Test

**With a CentOS or Fedora distributions**, to test the repository, you can use the command `yum list "metwork*"` (as `root`). You must get several `metwork-...` modules available.

??? question "For Mageia distributions?"
    To test the repository, you can use the command `urpmq --list |grep metwork |uniq` (as `root`). You must get several `metwork-...` modules available.

??? question "For SUSE distributions?"
    To test the repository, you can use the command `zypper pa |grep metwork` (as `root`). You must get several `metwork-...` modules available.

## How to install mfext metwork module

### Minimal installation

You just have to execute the following command (as `root` user):

```console tab="CentOS/Fedora"
yum install metwork-mfext
```

```console tab="Mageia"
urpmi metwork-mfext
```

```console tab="SUSE"
zypper install metwork-mfext
```




### Full installation (all mfext layers, except [add-ons]({{addons}}))


If you prefer a full installation (as `root` user):

```console tab="CentOS/Fedora"
yum install metwork-mfext-full
```

```console tab="Mageia"
urpmi metwork-mfext-full
```

```console tab="SUSE"
zypper install metwork-mfext-full
```




### Optional mfext layers

You can also add extra (optional) `mfext` layers.

```console tab="CentOS/Fedora"
# To install some devtools
yum install metwork-mfext-layer-python3_devtools

# To install some (base) scientific libraries
yum install metwork-mfext-layer-scientific_core

# To install python2 support
# (including corresponding scientific and devtools addons)
yum install metwork-mfext-layer-python2
yum install metwork-mfext-layer-python2_devtools

# To install java/nodejs binaries
yum install metwork-mfext-layer-nodejs
yum install metwork-mfext-layer-java
```

```console tab="Mageia"
# To install some devtools
urpmi metwork-mfext-layer-python3_devtools

# To install some (base) scientific libraries
urpmi metwork-mfext-layer-scientific_core

# To install python2 support
# (including corresponding scientific and devtools addons)
urpmi metwork-mfext-layer-python2
urpmi metwork-mfext-layer-python2_devtools

# To install java/nodejs binaries
urpmi metwork-mfext-layer-nodejs
urpmi metwork-mfext-layer-java
```

```console tab="SUSE"
# To install some devtools
zypper install metwork-mfext-layer-python3_devtools

# To install some (base) scientific libraries
zypper install metwork-mfext-layer-scientific_core

# To install python2 support
# (including corresponding scientific and devtools addons)
zypper install metwork-mfext-layer-python2
zypper install metwork-mfext-layer-python2_devtools

# To install java/nodejs binaries
zypper install metwork-mfext-layer-nodejs
zypper install metwork-mfext-layer-java
```

### Optional mfext layers (from mfext [add-ons]({{addons}}))

You can also install some optional layers (provided by some mfext [add-ons]({{addons}}))
in the same way and with the same repository (for official [add-ons]({{addons}})).

For example (please refer to corresponding add-on documentation)

```console tab="CentOS/Fedora"
# To install opinionated VIM with Python3 support
# for CentOS or Fedora (see above note for other distributions)
yum install metwork-mfext-layer-python3_vim

# To install all scientific libraries (for Python3)
yum install metwork-mfext-layer-python3_scientific

# To install "machine learning" Python3 libraries
yum install metwork-mfext-layer-python3_ia

# To install "mapserver" stuff for Python3
yum install metwork-mfext-layer-python3_mapserverapi

# [...]
```

```console tab="Mageia"
# To install opinionated VIM with Python3 support
# for CentOS or Fedora (see above note for other distributions)
urpmi metwork-mfext-layer-python3_vim

# To install all scientific libraries (for Python3)
urpmi metwork-mfext-layer-python3_scientific

# To install "machine learning" Python3 libraries
urpmi metwork-mfext-layer-python3_ia

# To install "mapserver" stuff for Python3
urpmi metwork-mfext-layer-python3_mapserverapi

# [...]
```

```console tab="SUSE"
# To install opinionated VIM with Python3 support
# for CentOS or Fedora (see above note for other distributions)
zypper install metwork-mfext-layer-python3_vim

# To install all scientific libraries (for Python3)
zypper install metwork-mfext-layer-python3_scientific

# To install "machine learning" Python3 libraries
zypper install metwork-mfext-layer-python3_ia

# To install "mapserver" stuff for Python3
zypper install metwork-mfext-layer-python3_mapserverapi

# [...]
```

## How to start all metwork modules (after installation)

```console
# As root user
service metwork start
```

!!! note
    If your distribution does not provide `service` command, you can use
    `systemctl start metwork.service` instead or `/etc/rc.d/init.d/metwork start`
    (if you don't have a `systemd` enabled machine or container).

## FAQ

### I don't want to install in `/opt`!

Sorry, but it's our packaging choice in it is coherent with [Linux FHS](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard). We have no plan to change that.

If you are really not happy with that, you can install MetWork
where you want by recompiling it.

### I don't have enough free space on `/opt`!

Let's say for example you have plenty of free space on `/data` but not in `/opt`, the recommended
way to install `mfext` is to:

- *(stop first all metwork services and apps using metwork (if any))*
- install a minimal `mfext` version (see corresponding chapter)
- move the `/opt/metwork-mfext-X.Y` directory to `/data` (`mv /opt/metwork-mfext-X.Y /data/`) to get a `/data/metwork-mfext-X.Y`
- add a symbolic link in `/opt` to get `/opt/metwork-mfext-X.Y => /data/metwork-mfext-X.Y` (`ln -s /data/metwork-mfext-X.Y /opt/metwork-mfext-X.Y`)
- install extra layers you want

With this procedure, you just need temporarily enough space in `/opt` to install
a minimal version. Then after the move and the symbolic link, this space is migrated to `/data` and all next installations will go in `/data`.

### How to install multiple versions of mfext module on the same machine?

You can install several "major/minor" versions (for example: `0.8.Z` and `0.9.T`)
of the mfext module on the same machine by configuring two package repositories
(one for `release_0.8` and one of `release_0.9`) and by using this special procedure:

```console tab="CentOS/Fedora"
yum install metwork-mfext-0.8
yum install metwork-mfext-0.9
```

```console tab="Mageia"
urpmi metwork-mfext-0.8
urpmi metwork-mfext-0.9
```

```console tab="SUSE"
zypper install metwork-mfext-0.8
zypper install metwork-mfext-0.9
```

!!! note
    You can add this `-X.Y` suffix to every "*mfext*" packages names (including
    optional layers and addons)

!!! warning
    You can't install several "patch" versions (for example: `0.8.1` and `0.8.2`)
    of the mfext module on the same machine. But but this is not usually a
    need because backward compatibility is guaranteed.

With this special procedure, you must not get a `/opt/metwork-mfext` symbolic link
but (only) two `/opt/metwork-mfext-0.8` and `/opt/metwork-mfext-0.9` directories.

Of course, to load the `mfext` profile, you have to point directly to the choosen
suffixed directory. So an app can load and use `mfext 0.8 ` and another one `mfext 0.9`.

### What about other modules?

This nearly works in same way but you have to:

- change the configuration of one version (at least) to changes listening ports to avoid
port collision during module startup
- start services by yourself

!!! warning
    This setup is not well tested but we are interested in. Please contact us
    if you want to share some experiences about that.
