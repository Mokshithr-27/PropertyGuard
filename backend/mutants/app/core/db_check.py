"""
PropertyGuard Database Health Diagnostic Check
------------------------------------------------
Provides a quick connectivity test function executing 'SELECT 1' against the
configured PostgreSQL database engine.
"""

from sqlalchemy import text

from app.core.database import engine


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_test_database_connection__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_test_database_connection__mutmut)
def test_database_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return result.scalar()


def x_test_database_connection__mutmut_orig():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return result.scalar()


def x_test_database_connection__mutmut_1():
    with engine.connect() as connection:
        result = None
        return result.scalar()


def x_test_database_connection__mutmut_2():
    with engine.connect() as connection:
        result = connection.execute(None)
        return result.scalar()


def x_test_database_connection__mutmut_3():
    with engine.connect() as connection:
        result = connection.execute(text(None))
        return result.scalar()


def x_test_database_connection__mutmut_4():
    with engine.connect() as connection:
        result = connection.execute(text("XXSELECT 1XX"))
        return result.scalar()


def x_test_database_connection__mutmut_5():
    with engine.connect() as connection:
        result = connection.execute(text("select 1"))
        return result.scalar()

mutants_x_test_database_connection__mutmut['_mutmut_orig'] = x_test_database_connection__mutmut_orig # type: ignore # mutmut generated
mutants_x_test_database_connection__mutmut['x_test_database_connection__mutmut_1'] = x_test_database_connection__mutmut_1 # type: ignore # mutmut generated
mutants_x_test_database_connection__mutmut['x_test_database_connection__mutmut_2'] = x_test_database_connection__mutmut_2 # type: ignore # mutmut generated
mutants_x_test_database_connection__mutmut['x_test_database_connection__mutmut_3'] = x_test_database_connection__mutmut_3 # type: ignore # mutmut generated
mutants_x_test_database_connection__mutmut['x_test_database_connection__mutmut_4'] = x_test_database_connection__mutmut_4 # type: ignore # mutmut generated
mutants_x_test_database_connection__mutmut['x_test_database_connection__mutmut_5'] = x_test_database_connection__mutmut_5 # type: ignore # mutmut generated