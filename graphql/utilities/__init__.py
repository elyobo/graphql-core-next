"""GraphQL Utilities

The :mod:`graphql.utilities` package contains common useful computations to use with
the GraphQL language and type objects.
"""

# The GraphQL query recommended for a full schema introspection.
from .introspection_query import get_introspection_query

# Gets the target Operation from a Document
from .get_operation_ast import get_operation_ast

# Gets the Type for the target Operation AST.
from .get_operation_root_type import get_operation_root_type

# Convert a GraphQLSchema to an IntrospectionQuery
from .introspection_from_schema import introspection_from_schema

# Build a GraphQLSchema from an introspection result.
from .build_client_schema import build_client_schema

# Build a GraphQLSchema from GraphQL Schema language.
from .build_ast_schema import build_ast_schema, build_schema, get_description

# Extends an existing GraphQLSchema from a parsed GraphQL Schema language AST.
from .extend_schema import extend_schema

# Sort a GraphQLSchema.
from .lexicographic_sort_schema import lexicographic_sort_schema

# Print a GraphQLSchema to GraphQL Schema language.
from .schema_printer import (
    print_introspection_schema,
    print_schema,
    print_type,
    print_value,
)

# Create a GraphQLType from a GraphQL language AST.
from .type_from_ast import type_from_ast

# Create a Python value from a GraphQL language AST with a type.
from .value_from_ast import value_from_ast

# Create a Python value from a GraphQL language AST without a type.
from .value_from_ast_untyped import value_from_ast_untyped

# Create a GraphQL language AST from a Python value.
from .ast_from_value import ast_from_value

# A helper to use within recursive-descent visitors which need to be aware of
# the GraphQL type system
from .type_info import TypeInfo

# Coerces a Python value to a GraphQL type, or produces errors.
from .coerce_value import coerce_value

# Concatenates multiple AST together.
from .concat_ast import concat_ast

# Separates an AST into an AST per Operation.
from .separate_operations import separate_operations

# Comparators for types
from .type_comparators import is_equal_type, is_type_sub_type_of, do_types_overlap

# Asserts that a string is a valid GraphQL name
from .assert_valid_name import assert_valid_name, is_valid_name_error

# Compares two GraphQLSchemas and detects breaking changes.
from .find_breaking_changes import (
    BreakingChange,
    BreakingChangeType,
    DangerousChange,
    DangerousChangeType,
    find_breaking_changes,
    find_dangerous_changes,
)

# Report all deprecated usage within a GraphQL document.
from .find_deprecated_usages import find_deprecated_usages

__all__ = [
    "BreakingChange",
    "BreakingChangeType",
    "DangerousChange",
    "DangerousChangeType",
    "TypeInfo",
    "assert_valid_name",
    "ast_from_value",
    "build_ast_schema",
    "build_client_schema",
    "build_schema",
    "coerce_value",
    "concat_ast",
    "do_types_overlap",
    "extend_schema",
    "find_breaking_changes",
    "find_dangerous_changes",
    "find_deprecated_usages",
    "get_description",
    "get_introspection_query",
    "get_operation_ast",
    "get_operation_root_type",
    "is_equal_type",
    "is_type_sub_type_of",
    "is_valid_name_error",
    "introspection_from_schema",
    "lexicographic_sort_schema",
    "print_introspection_schema",
    "print_schema",
    "print_type",
    "print_value",
    "separate_operations",
    "type_from_ast",
    "value_from_ast",
    "value_from_ast_untyped",
]
