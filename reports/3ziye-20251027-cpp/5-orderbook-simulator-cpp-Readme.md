# High-Performance Order Book Engine

A low-latency limit order book implementation in C++20 with real-time market data integration. Built to handle
high-frequency trading workloads with microsecond-level latency.

## Overview

This project implements a matching engine and order book that supports multiple order types, priority-based matching,
and real-time market data processing. The architecture is designed for performance-critical applications where latency
matters.

**Key metrics:**

- Order insertion: ~400,000 orders/sec
- Order matching: ~350,000 matches/sec
- Order cancellation: ~2,000,000 cancels/sec
- Average operation latency: 2-4 μs

## Features

### Core Order Book

- **Order Types**: GoodTillCancel, Market, ImmediateOrCancel, FillOrKill, GoodForDay
- **Matching Algorithm**: Price-time priority (FIFO within price levels)
- **Data Structures**: O(1) order lookup, O(log n) price level access
- **Trade Execution**: Automatic matching with partial fill support

### Market Data Feed

- Real-time orderbook snapshots via Binance REST API
- Incremental update processing (new orders, cancellations, modifications)
- Batch message processing for improved throughput
- Sequence number tracking for gap detection
- Latency monitoring and statistics

### Live Market Display

- Real-time visualization of cryptocurrency orderbooks
- Configurable refresh rates and depth levels
- Bid-ask spread analysis and mid-price calculation
- Market microstructure metrics

<img width="511" height="930" alt="image" src="https://github.com/user-attachments/assets/12dabc82-3a85-4cf9-8198-379178578fc4" />

## Build Instructions

### Requirements

- CMake 3.10+
- C++20 compatible compiler (GCC 10+, Clang 10+, MSVC 2019+)
- Dependencies (automatically fetched via CMake):
- libcurl 8.4.0
- nlohmann/json 3.11.3

### Build

```bash
mkdir build && cd build
cmake ..
cmake --build . --config Release
```

### Run

```bash
# Run functionality and performance tests
./OrderBookTests

# Live cryptocurrency orderbook
./LiveMarketData SOLUSDT 1 20
# Args: [SYMBOL] [REFRESH_SECONDS] [DEPTH_LEVELS]
```

## Architecture

### Class Diagram

```mermaid
classDiagram
    %% Core Type Aliases
    class Types {
        <<typedef>>
        +Price: int32_t
        +Quantity: uint32_t
        +OrderId: uint64_t
    }

    %% Enumerations
    class OrderType {
        <<enumeration>>
        GoodTillCancel
        ImmediateOrCancel
        Market
        GoodForDay
        FillOrKill
    }

    class Side {
        <<enumeration>>
        Buy
        Sell
    }

    class MessageType {
        <<enumeration>>
        NewOrder
        CancelOrder
        ModifyOrder
        Trade
        BookSnapshot
    }

    %% Constants
    class Constants {
        <<static>>
        +InvalidPrice: Price
    }

    %% Order Classes
    class Order {
        -orderType_: OrderType
        -orderId_: OrderId
        -side_: Side
        -price_: Price
        -initialQuantity_: Quantity
        -remainingQuantity_: Quantity
        +Order(OrderType, OrderId, Side, Price, Quantity)
        +Order(OrderId, Side, Quantity)
        +GetOrderId(): OrderId
        +GetSide(): Side
        +GetPrice(): Price
        +GetOrderType(): OrderType
        +GetInitialQuantity(): Quantity
        +GetRemainingQuantity(): Quantity
        +GetFilledQuantity(): Quantity
        +IsFilled(): bool
        +Fill(Quantity): void
        +ToGoodTillCancel(Price): void
    }

    class OrderModify {
        -orderId_: OrderId
        -price_: Price
        -side_: Side
        -quantity_: Quantity
        +OrderModify(OrderId, Side, Price, Quantity)
        +GetOrderId(): OrderId
        +GetPrice(): Price
        +GetSide(): Side
        +GetQuantity(): Quantity
        +ToOrderPointer(OrderType): OrderPointer
    }

    %% Trade Classes
    class TradeInfo {
        +orderId_: OrderId
        +price_: Price
        +quantity_: Quantity
    }

    class Trade {
        -bidTrade_: TradeInfo
        -askTrade_: TradeInfo
        +Trade(TradeInfo, TradeInfo)
        +GetBidTrade(): TradeInfo
        +GetAskTrade(): TradeInfo
    }

    %% Level Info Classes
    class LevelInfo {
        +price_: Price
        +quantity_: Quantity
    }

    class OrderbookLevelInfos {
        -bids_: LevelInfos
        -asks_: LevelInfos
        +OrderbookLevelInfos(LevelInfos, LevelInfos)
        +GetBids(): LevelInfos
        +GetAsks(): LevelInfos
    }

    %% Market Data Messages
    class NewOrderMessage {
        +type: MessageType
        +orderId: OrderId
        +side: Side
        +price: Price
        +quantity: Quantity
        +orderType: OrderType
        +timestamp: time_point
    }

    class CancelOrderMessage {
        +type: MessageType
        +orderId: OrderId
        +timestamp: time_point
    }

    class ModifyOrderMessage {
        +type: MessageType
        +orderId: OrderId
        +side: Side
        +newPrice: Price
        +newQuantity: Quantity
        +timestamp: time_point
    }