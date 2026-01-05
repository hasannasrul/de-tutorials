# Spark Basics (Interview-Friendly)

## Transformations — “what to do” steps
- Define how to change data; they **do not** run immediately.
- Common ones: `select`, `filter`, `withColumn`, `groupBy`, `agg`, `join`, `orderBy`, `repartition`, `coalesce`, `map`, `flatMap`.
- Narrow vs wide:
	- Narrow: each partition stays separate (e.g., `map`, `filter`). Faster, no shuffle.
	- Wide: need data shuffle across partitions (e.g., `groupBy`, `join`). Slower, network heavy.
- Interview tip: say “apply filters early, select only needed columns, avoid unnecessary shuffles.”

## Actions — “get the result” steps
- Trigger execution and return data or write it out.
- Common ones: `show`, `take`, `first`, `count`, `collect`, `foreach`, `save`, `write`.
- Interview tip: warn about `collect` on big data; prefer `show` with `limit` or `take` for quick checks.

## Lazy Evaluation — “wait until asked”
- Spark builds a DAG (plan) from transformations and waits until an action appears to run anything.
- Benefits: optimizer can reorder work, push filters down, prune columns, and combine steps before executing.
- Execution path: logical plan → optimized plan → physical plan → tasks on executors when an action starts.
- Interview tip: mention that caching (`cache`/`persist`) can speed repeated actions, but remember to `unpersist`.
