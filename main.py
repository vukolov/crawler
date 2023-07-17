from webcrawler.usecases.app import App
from webcrawler.external.file_storage import FileStorage
from webcrawler.external.web_site import WebSite
import argparse
from config import config
import validators


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-w',
                        '--workers',
                        type=int,
                        choices=range(config['min_workers_count'], config['max_workers_count'] + 1),
                        help='number of parallel processes',
                        default=config['default_workers_count'],
                        required=False)
    parser.add_argument('-u',
                        '--url',
                        type=str,
                        help='url to crawl',
                        required=True)
    args = parser.parse_args()
    if not validators.url(args.url):
        raise ValueError('Invalid url')
    app = App(
        workers_count=args.workers,
        data_sources=[WebSite(args.url)],
        storage=FileStorage(config['storage_path']),
        max_tasks=config['max_depth'])
    app.run()
