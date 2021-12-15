
all:
	@(cd sipgen; $(MAKE))
	@(cd siplib; $(MAKE))

install:
	@(cd sipgen; $(MAKE) install)
	@(cd siplib; $(MAKE) install)
	@test -d $(DESTDIR)/usr/lib/python2.7/dist-packages || mkdir -p $(DESTDIR)/usr/lib/python2.7/dist-packages
	cp -f sipconfig.py $(DESTDIR)/usr/lib/python2.7/dist-packages/sipconfig.py
	cp -f /home/pi/train-system/sip-4.19.24/sipdistutils.py $(DESTDIR)/usr/lib/python2.7/dist-packages/sipdistutils.py
	/usr/bin/python /home/pi/train-system/sip-4.19.24/mk_distinfo.py "$(DESTDIR)" /usr/lib/python2.7/dist-packages/sip-4.19.24.dist-info installed.txt

clean:
	@(cd sipgen; $(MAKE) clean)
	@(cd siplib; $(MAKE) clean)
