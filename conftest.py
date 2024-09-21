import pytest

from data.data_orders import payload_order
from endpoint.couriers.create_courier import CreateCourier
from endpoint.couriers.delete_courier import DeleteCourier
from endpoint.couriers.get_courier_id import GetCourierId
from data.data_create_courier import payload_create_courier
from endpoint.orders.create_order import CreateOrder
from endpoint.orders.delete_order import DeleteOrder


@pytest.fixture()
def prepare_courier():
    create = CreateCourier()
    create.create_courier(payload_create_courier)

    get = GetCourierId()
    get.get_id(payload_create_courier)

    yield get.id, payload_create_courier

    delete = DeleteCourier()
    delete.delete_courier(get.id)
    delete.response_is(200)


@pytest.fixture()
def create_courier_for_test_delete():
    create = CreateCourier()
    create.create_courier(payload_create_courier)

    get = GetCourierId()
    get.get_id(payload_create_courier)
    return get.id


@pytest.fixture()
def prepare_order():
    create = CreateOrder()
    create.create_order(payload_order)
    create.response_is(201)
    yield create.track

    delete = DeleteOrder()
    delete.cancel_order(create.response_json)
    delete.response_is(200)
