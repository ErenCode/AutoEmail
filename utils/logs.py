import os
import multiprocessing
import logging
import datetime

def init_logger(name, subname='default', workspace='./%s', multiproc=False, file_level=None, stream_level=None):
    workspace = os.path.abspath(workspace)
    w = os.path.dirname(workspace)
    if not os.path.exists(w):
        os.makedirs(w)
    if multiproc:
        log = multiprocessing.get_logger()
    else:
        log = logging.getLogger(name)

    log.setLevel(logging.DEBUG)
    fmt = logging.Formatter(r'[%(levelname)s][%(asctime)s %(filename)s:%(lineno)d] %(message)s')

    if stream_level:
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(stream_level)
        log.addHandler(sh)
    else:
        sh = None

    if file_level:

        workspace_dir = os.path.dirname(workspace)
        if not os.path.exists(workspace_dir):
            os.makedirs(workspace_dir)

        fh = logging.FileHandler(
            workspace % ('%s-%s.log' % (subname, datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')),))
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        log.addHandler(fh)
    else:
        fh = None

    return log, sh, fh
