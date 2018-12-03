# Stubs for pandas.io.pytables (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from pandas.core.base import StringMixin
from pandas.core.computation.pytables import Expr
from typing import Any, Optional

Term = Expr

class PossibleDataLossError(Exception): ...
class ClosedFileError(Exception): ...
class IncompatibilityWarning(Warning): ...

incompatibility_doc: str

class AttributeConflictWarning(Warning): ...

attribute_conflict_doc: str

class DuplicateWarning(Warning): ...

duplicate_doc: str
performance_doc: str
format_deprecate_doc: str
dropna_doc: str
format_doc: str

def to_hdf(path_or_buf: Any, key: Any, value: Any, mode: Optional[Any] = ..., complevel: Optional[Any] = ..., complib: Optional[Any] = ..., append: Optional[Any] = ..., **kwargs: Any): ...
def read_hdf(path_or_buf: Any, key: Optional[Any] = ..., mode: str = ..., **kwargs: Any): ...

class HDFStore(StringMixin):
    def __init__(self, path: Any, mode: Optional[Any] = ..., complevel: Optional[Any] = ..., complib: Optional[Any] = ..., fletcher32: bool = ..., **kwargs: Any) -> None: ...
    def __fspath__(self): ...
    @property
    def root(self): ...
    @property
    def filename(self): ...
    def __getitem__(self, key: Any): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __delitem__(self, key: Any): ...
    def __getattr__(self, name: Any): ...
    def __contains__(self, key: Any): ...
    def __len__(self): ...
    def __unicode__(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: ...
    def keys(self): ...
    def __iter__(self): ...
    def items(self) -> None: ...
    iteritems: Any = ...
    def open(self, mode: str = ..., **kwargs: Any) -> None: ...
    def close(self) -> None: ...
    @property
    def is_open(self): ...
    def flush(self, fsync: bool = ...) -> None: ...
    def get(self, key: Any): ...
    def select(self, key: Any, where: Optional[Any] = ..., start: Optional[Any] = ..., stop: Optional[Any] = ..., columns: Optional[Any] = ..., iterator: bool = ..., chunksize: Optional[Any] = ..., auto_close: bool = ..., **kwargs: Any): ...
    def select_as_coordinates(self, key: Any, where: Optional[Any] = ..., start: Optional[Any] = ..., stop: Optional[Any] = ..., **kwargs: Any): ...
    def select_column(self, key: Any, column: Any, **kwargs: Any): ...
    def select_as_multiple(self, keys: Any, where: Optional[Any] = ..., selector: Optional[Any] = ..., columns: Optional[Any] = ..., start: Optional[Any] = ..., stop: Optional[Any] = ..., iterator: bool = ..., chunksize: Optional[Any] = ..., auto_close: bool = ..., **kwargs: Any): ...
    def put(self, key: Any, value: Any, format: Optional[Any] = ..., append: bool = ..., **kwargs: Any) -> None: ...
    def remove(self, key: Any, where: Optional[Any] = ..., start: Optional[Any] = ..., stop: Optional[Any] = ...): ...
    def append(self, key: Any, value: Any, format: Optional[Any] = ..., append: bool = ..., columns: Optional[Any] = ..., dropna: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def append_to_multiple(self, d: Any, value: Any, selector: Any, data_columns: Optional[Any] = ..., axes: Optional[Any] = ..., dropna: bool = ..., **kwargs: Any) -> None: ...
    def create_table_index(self, key: Any, **kwargs: Any): ...
    def groups(self): ...
    def walk(self, where: str = ...) -> None: ...
    def get_node(self, key: Any): ...
    def get_storer(self, key: Any): ...
    def copy(self, file: Any, mode: str = ..., propindexes: bool = ..., keys: Optional[Any] = ..., complib: Optional[Any] = ..., complevel: Optional[Any] = ..., fletcher32: bool = ..., overwrite: bool = ...): ...
    def info(self): ...

class TableIterator:
    store: Any = ...
    s: Any = ...
    func: Any = ...
    where: Any = ...
    nrows: Any = ...
    start: Any = ...
    stop: Any = ...
    coordinates: Any = ...
    chunksize: Any = ...
    auto_close: Any = ...
    def __init__(self, store: Any, s: Any, func: Any, where: Any, nrows: Any, start: Optional[Any] = ..., stop: Optional[Any] = ..., iterator: bool = ..., chunksize: Optional[Any] = ..., auto_close: bool = ...) -> None: ...
    def __iter__(self) -> None: ...
    def close(self) -> None: ...
    def get_result(self, coordinates: bool = ...): ...

class IndexCol(StringMixin):
    is_an_indexable: bool = ...
    is_data_indexable: bool = ...
    values: Any = ...
    kind: Any = ...
    typ: Any = ...
    itemsize: Any = ...
    name: Any = ...
    cname: Any = ...
    kind_attr: Any = ...
    axis: Any = ...
    pos: Any = ...
    freq: Any = ...
    tz: Any = ...
    index_name: Any = ...
    table: Any = ...
    meta: Any = ...
    metadata: Any = ...
    def __init__(self, values: Optional[Any] = ..., kind: Optional[Any] = ..., typ: Optional[Any] = ..., cname: Optional[Any] = ..., itemsize: Optional[Any] = ..., name: Optional[Any] = ..., axis: Optional[Any] = ..., kind_attr: Optional[Any] = ..., pos: Optional[Any] = ..., freq: Optional[Any] = ..., tz: Optional[Any] = ..., index_name: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def set_name(self, name: Any, kind_attr: Optional[Any] = ...): ...
    def set_axis(self, axis: Any): ...
    def set_pos(self, pos: Any): ...
    def set_table(self, table: Any): ...
    def __unicode__(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    @property
    def is_indexed(self): ...
    def copy(self): ...
    def infer(self, handler: Any): ...
    def convert(self, values: Any, nan_rep: Any, encoding: Any, errors: Any): ...
    def take_data(self): ...
    @property
    def attrs(self): ...
    @property
    def description(self): ...
    @property
    def col(self): ...
    @property
    def cvalues(self): ...
    def __iter__(self): ...
    def maybe_set_size(self, min_itemsize: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def validate(self, handler: Any, append: Any, **kwargs: Any) -> None: ...
    def validate_names(self) -> None: ...
    def validate_and_set(self, handler: Any, append: Any, **kwargs: Any) -> None: ...
    def validate_col(self, itemsize: Optional[Any] = ...): ...
    def validate_attr(self, append: Any) -> None: ...
    def update_info(self, info: Any): ...
    def set_info(self, info: Any) -> None: ...
    def get_attr(self) -> None: ...
    def set_attr(self) -> None: ...
    def read_metadata(self, handler: Any) -> None: ...
    def validate_metadata(self, handler: Any) -> None: ...
    def write_metadata(self, handler: Any) -> None: ...

class GenericIndexCol(IndexCol):
    @property
    def is_indexed(self): ...
    values: Any = ...
    def convert(self, values: Any, nan_rep: Any, encoding: Any, errors: Any): ...
    def get_attr(self) -> None: ...
    def set_attr(self) -> None: ...

class DataCol(IndexCol):
    is_an_indexable: bool = ...
    is_data_indexable: bool = ...
    @classmethod
    def create_for_block(cls, i: Optional[Any] = ..., name: Optional[Any] = ..., cname: Optional[Any] = ..., version: Optional[Any] = ..., **kwargs: Any): ...
    dtype: Any = ...
    dtype_attr: Any = ...
    meta: Any = ...
    meta_attr: Any = ...
    def __init__(self, values: Optional[Any] = ..., kind: Optional[Any] = ..., typ: Optional[Any] = ..., cname: Optional[Any] = ..., data: Optional[Any] = ..., meta: Optional[Any] = ..., metadata: Optional[Any] = ..., block: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def __unicode__(self): ...
    def __eq__(self, other: Any): ...
    data: Any = ...
    def set_data(self, data: Any, dtype: Optional[Any] = ...) -> None: ...
    def take_data(self): ...
    metadata: Any = ...
    def set_metadata(self, metadata: Any) -> None: ...
    kind: str = ...
    typ: Any = ...
    def set_kind(self) -> None: ...
    values: Any = ...
    def set_atom(self, block: Any, block_items: Any, existing_col: Any, min_itemsize: Any, nan_rep: Any, info: Any, encoding: Optional[Any] = ..., errors: str = ...): ...
    def get_atom_string(self, block: Any, itemsize: Any): ...
    itemsize: Any = ...
    def set_atom_string(self, block: Any, block_items: Any, existing_col: Any, min_itemsize: Any, nan_rep: Any, encoding: Any, errors: Any) -> None: ...
    def get_atom_coltype(self, kind: Optional[Any] = ...): ...
    def get_atom_data(self, block: Any, kind: Optional[Any] = ...): ...
    def set_atom_complex(self, block: Any) -> None: ...
    def set_atom_data(self, block: Any) -> None: ...
    ordered: Any = ...
    def set_atom_categorical(self, block: Any, items: Any, info: Optional[Any] = ..., values: Optional[Any] = ...) -> None: ...
    def get_atom_datetime64(self, block: Any): ...
    def set_atom_datetime64(self, block: Any, values: Optional[Any] = ...) -> None: ...
    tz: Any = ...
    def set_atom_datetime64tz(self, block: Any, info: Any, values: Optional[Any] = ...) -> None: ...
    def get_atom_timedelta64(self, block: Any): ...
    def set_atom_timedelta64(self, block: Any, values: Optional[Any] = ...) -> None: ...
    @property
    def shape(self): ...
    @property
    def cvalues(self): ...
    def validate_attr(self, append: Any) -> None: ...
    def convert(self, values: Any, nan_rep: Any, encoding: Any, errors: Any): ...
    def get_attr(self) -> None: ...
    def set_attr(self) -> None: ...

class DataIndexableCol(DataCol):
    is_data_indexable: bool = ...
    def validate_names(self) -> None: ...
    def get_atom_string(self, block: Any, itemsize: Any): ...
    def get_atom_data(self, block: Any, kind: Optional[Any] = ...): ...
    def get_atom_datetime64(self, block: Any): ...
    def get_atom_timedelta64(self, block: Any): ...

class GenericDataIndexableCol(DataIndexableCol):
    def get_attr(self) -> None: ...

class Fixed(StringMixin):
    pandas_kind: Any = ...
    obj_type: Any = ...
    ndim: Any = ...
    is_table: bool = ...
    parent: Any = ...
    group: Any = ...
    encoding: Any = ...
    errors: Any = ...
    def __init__(self, parent: Any, group: Any, encoding: Optional[Any] = ..., errors: str = ..., **kwargs: Any) -> None: ...
    @property
    def is_old_version(self): ...
    version: Any = ...
    def set_version(self) -> None: ...
    @property
    def pandas_type(self): ...
    @property
    def format_type(self): ...
    def __unicode__(self): ...
    def set_object_info(self) -> None: ...
    def copy(self): ...
    @property
    def storage_obj_type(self): ...
    @property
    def shape(self): ...
    @property
    def pathname(self): ...
    @property
    def attrs(self): ...
    def set_attrs(self) -> None: ...
    def get_attrs(self) -> None: ...
    @property
    def storable(self): ...
    @property
    def is_exists(self): ...
    @property
    def nrows(self): ...
    def validate(self, other: Any): ...
    def validate_version(self, where: Optional[Any] = ...): ...
    def infer_axes(self): ...
    def read(self, **kwargs: Any) -> None: ...
    def write(self, **kwargs: Any) -> None: ...
    def delete(self, where: Optional[Any] = ..., start: Optional[Any] = ..., stop: Optional[Any] = ..., **kwargs: Any): ...

class GenericFixed(Fixed):
    attributes: Any = ...
    def validate_read(self, kwargs: Any): ...
    @property
    def is_exists(self): ...
    def set_attrs(self) -> None: ...
    encoding: Any = ...
    errors: Any = ...
    def get_attrs(self) -> None: ...
    def write(self, obj: Any, **kwargs: Any) -> None: ...
    def read_array(self, key: Any, start: Optional[Any] = ..., stop: Optional[Any] = ...): ...
    def read_index(self, key: Any, **kwargs: Any): ...
    def write_index(self, key: Any, index: Any) -> None: ...
    def write_block_index(self, key: Any, index: Any) -> None: ...
    def read_block_index(self, key: Any, **kwargs: Any): ...
    def write_sparse_intindex(self, key: Any, index: Any) -> None: ...
    def read_sparse_intindex(self, key: Any, **kwargs: Any): ...
    def write_multi_index(self, key: Any, index: Any) -> None: ...
    def read_multi_index(self, key: Any, **kwargs: Any): ...
    def read_index_node(self, node: Any, start: Optional[Any] = ..., stop: Optional[Any] = ...): ...
    def write_array_empty(self, key: Any, value: Any) -> None: ...
    def write_array(self, key: Any, value: Any, items: Optional[Any] = ...): ...

class LegacyFixed(GenericFixed):
    def read_index_legacy(self, key: Any, start: Optional[Any] = ..., stop: Optional[Any] = ...): ...

class LegacySeriesFixed(LegacyFixed):
    def read(self, **kwargs: Any): ...

class LegacyFrameFixed(LegacyFixed):
    def read(self, **kwargs: Any): ...

class SeriesFixed(GenericFixed):
    pandas_kind: str = ...
    attributes: Any = ...
    @property
    def shape(self): ...
    def read(self, **kwargs: Any): ...
    def write(self, obj: Any, **kwargs: Any) -> None: ...

class SparseFixed(GenericFixed):
    def validate_read(self, kwargs: Any): ...

class SparseSeriesFixed(SparseFixed):
    pandas_kind: str = ...
    attributes: Any = ...
    def read(self, **kwargs: Any): ...
    def write(self, obj: Any, **kwargs: Any) -> None: ...

class SparseFrameFixed(SparseFixed):
    pandas_kind: str = ...
    attributes: Any = ...
    def read(self, **kwargs: Any): ...
    def write(self, obj: Any, **kwargs: Any) -> None: ...

class BlockManagerFixed(GenericFixed):
    attributes: Any = ...
    is_shape_reversed: bool = ...
    @property
    def shape(self): ...
    def read(self, start: Optional[Any] = ..., stop: Optional[Any] = ..., **kwargs: Any): ...
    def write(self, obj: Any, **kwargs: Any) -> None: ...

class FrameFixed(BlockManagerFixed):
    pandas_kind: str = ...
    obj_type: Any = ...

class PanelFixed(BlockManagerFixed):
    pandas_kind: str = ...
    obj_type: Any = ...
    is_shape_reversed: bool = ...
    def write(self, obj: Any, **kwargs: Any): ...

class Table(Fixed):
    pandas_kind: str = ...
    table_type: Any = ...
    levels: int = ...
    is_table: bool = ...
    is_shape_reversed: bool = ...
    index_axes: Any = ...
    non_index_axes: Any = ...
    values_axes: Any = ...
    data_columns: Any = ...
    metadata: Any = ...
    info: Any = ...
    nan_rep: Any = ...
    selection: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @property
    def table_type_short(self): ...
    @property
    def format_type(self): ...
    def __unicode__(self): ...
    def __getitem__(self, c: Any): ...
    def validate(self, other: Any): ...
    @property
    def is_multi_index(self): ...
    def validate_metadata(self, existing: Any) -> None: ...
    def validate_multiindex(self, obj: Any): ...
    @property
    def nrows_expected(self): ...
    @property
    def is_exists(self): ...
    @property
    def storable(self): ...
    @property
    def table(self): ...
    @property
    def dtype(self): ...
    @property
    def description(self): ...
    @property
    def axes(self): ...
    @property
    def ncols(self): ...
    @property
    def is_transposed(self): ...
    @property
    def data_orientation(self): ...
    def queryables(self): ...
    def index_cols(self): ...
    def values_cols(self): ...
    def write_metadata(self, key: Any, values: Any) -> None: ...
    def read_metadata(self, key: Any): ...
    def set_info(self) -> None: ...
    def set_attrs(self) -> None: ...
    encoding: Any = ...
    errors: Any = ...
    def get_attrs(self) -> None: ...
    def validate_version(self, where: Optional[Any] = ...) -> None: ...
    def validate_min_itemsize(self, min_itemsize: Any): ...
    @property
    def indexables(self): ...
    def create_index(self, columns: Optional[Any] = ..., optlevel: Optional[Any] = ..., kind: Optional[Any] = ...): ...
    def read_axes(self, where: Any, **kwargs: Any): ...
    def get_object(self, obj: Any): ...
    def validate_data_columns(self, data_columns: Any, min_itemsize: Any): ...
    def create_axes(self, axes: Any, obj: Any, validate: bool = ..., nan_rep: Optional[Any] = ..., data_columns: Optional[Any] = ..., min_itemsize: Optional[Any] = ..., **kwargs: Any): ...
    def process_axes(self, obj: Any, columns: Optional[Any] = ...): ...
    def create_description(self, complib: Optional[Any] = ..., complevel: Optional[Any] = ..., fletcher32: bool = ..., expectedrows: Optional[Any] = ...): ...
    def read_coordinates(self, where: Optional[Any] = ..., start: Optional[Any] = ..., stop: Optional[Any] = ..., **kwargs: Any): ...
    def read_column(self, column: Any, where: Optional[Any] = ..., start: Optional[Any] = ..., stop: Optional[Any] = ..., **kwargs: Any): ...

class WORMTable(Table):
    table_type: str = ...
    def read(self, **kwargs: Any) -> None: ...
    def write(self, **kwargs: Any) -> None: ...

class LegacyTable(Table):
    table_type: str = ...
    ndim: int = ...
    def write(self, **kwargs: Any) -> None: ...
    def read(self, where: Optional[Any] = ..., columns: Optional[Any] = ..., **kwargs: Any): ...

class LegacyFrameTable(LegacyTable):
    pandas_kind: str = ...
    table_type: str = ...
    obj_type: Any = ...
    def read(self, *args: Any, **kwargs: Any): ...

class LegacyPanelTable(LegacyTable):
    table_type: str = ...
    obj_type: Any = ...

class AppendableTable(LegacyTable):
    table_type: str = ...
    def write(self, obj: Any, axes: Optional[Any] = ..., append: bool = ..., complib: Optional[Any] = ..., complevel: Optional[Any] = ..., fletcher32: Optional[Any] = ..., min_itemsize: Optional[Any] = ..., chunksize: Optional[Any] = ..., expectedrows: Optional[Any] = ..., dropna: bool = ..., **kwargs: Any) -> None: ...
    def write_data(self, chunksize: Any, dropna: bool = ...) -> None: ...
    def write_data_chunk(self, rows: Any, indexes: Any, mask: Any, values: Any): ...
    selection: Any = ...
    def delete(self, where: Optional[Any] = ..., start: Optional[Any] = ..., stop: Optional[Any] = ..., **kwargs: Any): ...

class AppendableFrameTable(AppendableTable):
    pandas_kind: str = ...
    table_type: str = ...
    ndim: int = ...
    obj_type: Any = ...
    @property
    def is_transposed(self): ...
    def get_object(self, obj: Any): ...
    def read(self, where: Optional[Any] = ..., columns: Optional[Any] = ..., **kwargs: Any): ...

class AppendableSeriesTable(AppendableFrameTable):
    pandas_kind: str = ...
    table_type: str = ...
    ndim: int = ...
    obj_type: Any = ...
    storage_obj_type: Any = ...
    @property
    def is_transposed(self): ...
    def get_object(self, obj: Any): ...
    def write(self, obj: Any, data_columns: Optional[Any] = ..., **kwargs: Any): ...
    def read(self, columns: Optional[Any] = ..., **kwargs: Any): ...

class AppendableMultiSeriesTable(AppendableSeriesTable):
    pandas_kind: str = ...
    table_type: str = ...
    def write(self, obj: Any, **kwargs: Any): ...

class GenericTable(AppendableFrameTable):
    pandas_kind: str = ...
    table_type: str = ...
    ndim: int = ...
    obj_type: Any = ...
    @property
    def pandas_type(self): ...
    @property
    def storable(self): ...
    non_index_axes: Any = ...
    nan_rep: Any = ...
    levels: Any = ...
    index_axes: Any = ...
    values_axes: Any = ...
    data_columns: Any = ...
    def get_attrs(self) -> None: ...
    @property
    def indexables(self): ...
    def write(self, **kwargs: Any) -> None: ...

class AppendableMultiFrameTable(AppendableFrameTable):
    table_type: str = ...
    obj_type: Any = ...
    ndim: int = ...
    @property
    def table_type_short(self): ...
    def write(self, obj: Any, data_columns: Optional[Any] = ..., **kwargs: Any): ...
    def read(self, **kwargs: Any): ...

class AppendablePanelTable(AppendableTable):
    table_type: str = ...
    ndim: int = ...
    obj_type: Any = ...
    def get_object(self, obj: Any): ...
    @property
    def is_transposed(self): ...

class Selection:
    table: Any = ...
    where: Any = ...
    start: Any = ...
    stop: Any = ...
    condition: Any = ...
    filter: Any = ...
    terms: Any = ...
    coordinates: Any = ...
    def __init__(self, table: Any, where: Optional[Any] = ..., start: Optional[Any] = ..., stop: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def generate(self, where: Any): ...
    def select(self): ...
    def select_coords(self): ...

def timeit(key: Any, df: Any, fn: Optional[Any] = ..., remove: bool = ..., **kwargs: Any) -> None: ...
