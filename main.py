from webcrawler.usecases.app import App
from webcrawler.external.file_storage import FileStorage
from webcrawler.external.web_site import WebSite
import argparse
import logging
from config import config


if __name__ == '__main__':
    logging.info('Starting', {'tag': 'operation'})
    parser = argparse.ArgumentParser()
    parser.add_argument('-w',
                        '--workers',
                        type=int,
                        choices=range(config['min_workers_count'], config['max_workers_count'] + 1),
                        help='number of parallel processes',
                        required=False)
    parser.add_argument('-u',
                        '--url',
                        type=str,
                        help='url to crawl',
                        required=True)
    args = parser.parse_args()
    workers = config['default_workers_count']
    if args.workers:
        workers = args.workers
    app = App(
        workers_count=workers,
        data_sources=[WebSite(args.url)],
        storage=FileStorage(config['storage_path']))
    app.run()
