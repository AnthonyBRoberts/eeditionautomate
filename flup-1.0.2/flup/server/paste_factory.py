# (c) 2005 Ian Bicking and contributors; written for Paste (http://pythonpaste.org)
# Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php
def asbool(obj):
    if isinstance(obj, (str, unicode)):
        obj = obj.strip().lower()
        if obj in ['true', 'yes', 'on', 'y', 't', '1']:
            return True
        elif obj in ['false', 'no', 'off', 'n', 'f', '0']:
            return False
        else:
            raise ValueError(
                "String is not true/false: %r" % obj)
    return bool(obj)

def aslist(obj, sep=None, strip=True):
    if isinstance(obj, (str, unicode)):
        lst = obj.split(sep)
        if strip:
            lst = [v.strip() for v in lst]
        return lst
    elif isinstance(obj, (list, tuple)):
        return obj
    elif obj is None:
        return []
    else:
        return [obj]

def run_ajp_thread(wsgi_app, global_conf,
                   scriptName='', host='localhost', port='8009',
                   allowedServers='127.0.0.1'):
    import flup.server.ajp
    addr = (host, int(port))
    s = flup.server.ajp.WSGIServer(
        wsgi_app,
        scriptName=scriptName,
        bindAddress=addr,
        allowedServers=aslist(allowedServers),
        )
    s.run()
    
def run_ajp_fork(wsgi_app, global_conf,
                 scriptName='', host='localhost', port='8009',
                 allowedServers='127.0.0.1'):
    import flup.server.ajp_fork
    addr = (host, int(port))
    s = flup.server.ajp_fork.WSGIServer(
        wsgi_app,
        scriptName=scriptName,
        bindAddress=addr,
        allowedServers=aslist(allowedServers),
        )
    s.run()

def run_fcgi_thread(wsgi_app, global_conf,
                    host=None, port=None,
                    socket=None, umask=None,
                    multiplexed=False):
    import flup.server.fcgi
    if socket:
        assert host is None and port is None
        sock = socket
    elif host:
        assert host is not None and port is not None
        sock = (host, int(port))
    else:
        sock = None
    if umask is not None:
        umask = int(umask)
    s = flup.server.fcgi.WSGIServer(
        wsgi_app,
        bindAddress=sock, umask=umask,
        multiplexed=asbool(multiplexed))
    s.run()

def run_fcgi_fork(wsgi_app, global_conf,
                  host=None, port=None,
                  socket=None, umask=None,
                  multiplexed=False):
    import flup.server.fcgi_fork
    if socket:
        assert host is None and port is None
        sock = socket
    elif host:
        assert host is not None and port is not None
        sock = (host, int(port))
    else:
        sock = None
    if umask is not None:
        umask = int(umask)
    s = flup.server.fcgi_fork.WSGIServer(
        wsgi_app,
        bindAddress=sock, umask=umask,
        multiplexed=asbool(multiplexed))
    s.run()

def run_scgi_thread(wsgi_app, global_conf,
                    scriptName='', host='localhost', port='4000',
                    allowedServers='127.0.0.1'):
    import flup.server.scgi
    addr = (host, int(port))
    s = flup.server.scgi.WSGIServer(
        wsgi_app,
        scriptName=scriptName,
        bindAddress=addr,
        allowedServers=aslist(allowedServers),
        )
    s.run()

def run_scgi_fork(wsgi_app, global_conf,
                  scriptName='', host='localhost', port='4000',
                  allowedServers='127.0.0.1'):
    import flup.server.scgi_fork
    addr = (host, int(port))
    s = flup.server.scgi_fork.WSGIServer(
        wsgi_app,
        scriptName=scriptName,
        bindAddress=addr,
        allowedServers=aslist(allowedServers),
        )
    s.run()
    
