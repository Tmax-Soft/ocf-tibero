# ocf-tibero

Resource script for Tibero database for Pacemaker (Red Hat Cluster Suite)

## Usage

Copy script to /usr/lib/ocf/resource.d/heartbeat/ manually or build and install rpm package, than create tibero database resource:

```
pcs resource create tibero_db ocf:heartbeat:tibero tb_owner=tibero \
  tb_home=/opt/tibero/Tibero/tibero5 tb_sid=TBSID tb_user=cluster tb_password=password
```

## Parameters
 - tb_home - Tibero home directory ($TB_HOME)
 - tb_owner - Tibero owner (OS user)
 - tb_sid - Tibero SID ($TB_SID)
 - tb_user - Tibero database user (with sysdba privilege).
 - tb_password - tb_user's password.
