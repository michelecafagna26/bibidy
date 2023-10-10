import click
from pathlib import Path
from pybtex.database.input import bibtex
from pybtex.database import BibliographyData
from copy import deepcopy


def load_bib(psx):
    parser = bibtex.Parser()
    bib_data = parser.parse_file(psx)
    return bib_data


def save_bib(bib, filename, style="bibtex"):
    with open(filename, "w", encoding="utf-8") as fp:
        fp.write(bib.to_string(style).replace("\\\\", "\\"))


def merge_bibs(bibs):
    new_bib = deepcopy(bibs[0])

    for bib in bibs:
        for k in bib.entries:
            if k not in new_bib.entries:
                new_bib.add_entry(key=k, entry=bib.entries[k])
    return new_bib


def intersect_bibs(bibs):
    new_bib = BibliographyData()

    shared_set = set(bibs[0].entries.keys())
    for bib in bibs[1:]:
        shared_set = shared_set.intersection(set(bib.entries.keys()))

    for bib in bibs:
        for k in bib.entries:
            if k not in new_bib.entries and k in shared_set:
                new_bib.add_entry(key=k, entry=bib.entries[k])

    return new_bib


@click.group()
def bibidy():
    pass

@bibidy.command()
@click.argument('in_bibs', nargs=-1)
def count(in_bibs):
    """Count the number of entries in the bibfile/s """

    in_bibs = in_bibs[0].split(",")
    bibs = [load_bib(Path(bib_fn)) for bib_fn in in_bibs]

    for fn, bib in zip(in_bibs,bibs):
        click.echo(f"{Path(fn).name} : {len(bib.entries)} entries")

@bibidy.command()
@click.argument('in_bibs', nargs=-1)
@click.option('--out', default="out.bib", help='output_filename.')
def merge(in_bibs, out):
    """Merge a list of bib files into one"""

    in_bibs = in_bibs[0].split(",")
    bibs = [load_bib(Path(bib_fn)) for bib_fn in in_bibs]

    new_bib = merge_bibs(bibs)
    click.echo(f"Created a new bibfile with {len(new_bib.entries)} entries")

    save_bib(new_bib, out)
    click.echo(f"New bibfile saved in {out}")


@bibidy.command()
@click.argument('in_bibs', nargs=-1)
@click.option('--out', default="out.bib", help='output filename.')
def intersect(in_bibs, out):
    """Intersect a list of bib files; It returns a bib files with the shared set of refs"""

    in_bibs = in_bibs[0].split(",")
    bibs = [load_bib(Path(bib_fn)) for bib_fn in in_bibs]

    new_bib = intersect_bibs(bibs)
    click.echo(f"Created a new bibfile with {len(new_bib.entries)} entries")

    save_bib(new_bib, out)
    click.echo(f"New bibfile saved in {out}")


cli = click.CommandCollection(sources=[bibidy])
if __name__ == "__main__":
    cli()
