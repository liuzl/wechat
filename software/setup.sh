ES='elasticsearch-5.3.1.tar.gz'
DES='elasticsearch-5.3.1'
KIBANA='kibana-5.3.1-darwin-x86_64.tar.gz'
DKIBANA='kibana-5.3.1-darwin-x86_64'

# 下载elasticsearch和kibana
if [ ! -f "${ES}" ] ; then
    wget https://artifacts.elastic.co/downloads/elasticsearch/${ES}
else
    echo "${ES} already downloaded"
fi

if [ ! -f "$KIBANA" ] ; then
    wget https://artifacts.elastic.co/downloads/kibana/${KIBANA}
else
    echo "$KIBANA already downloaded"
fi

# 解压
if [ ! -d "${DES}" ] ; then
    tar -xvzf ${ES}
fi

if [ ! -d "${DKIBANA}" ] ; then
    tar -xvzf ${KIBANA}
fi

# 安装x-pack
#cd $DES
#bin/elasticsearch-plugin install x-pack
#cd -

#cd $DKIBANA
#bin/kibana-plugin install x-pack
#cd -
